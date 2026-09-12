from typing import List
from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
        # Sort original indices by the right endpoints of their intervals
        order = sorted(range(n), key=lambda i: intervals[i][1])
        rights = [intervals[i][1] for i in order]
        
        # prev array stores tuples of (negative_score, list_of_indices)
        # Using a negative score ensures that min() prioritizes the maximum score 
        # and inherently breaks ties with the lexicographically smaller list.
        prev = [(0, [])] * (n + 1)
        
        # We can pick at most 4 intervals
        for _ in range(4):
            cur = [(0, [])] * (n + 1)
            for p in range(1, n + 1):
                i = order[p - 1]
                l, r, w = intervals[i]
                
                # Binary search to find intervals that end strictly before the current one starts
                j = bisect_left(rights, l)
                
                # DP Transition:
                # Option 1: Take the current interval (add its weight and index, then sort indices)
                score, ids = prev[j]
                take_interval = (score - w, sorted(ids + [i]))
                
                # Option 2: Skip this interval and keep the best from the previous steps
                skip_interval = cur[p - 1]
                
                # Keep the optimal choice for this subproblem
                cur[p] = min(take_interval, skip_interval)
                
            prev = cur
            
        return prev[n][1]