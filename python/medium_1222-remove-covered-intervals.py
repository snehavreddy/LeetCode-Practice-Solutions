class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort: ascending by start, then descending by end
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        count = 0
        max_r = 0
        
        for _, r in intervals:
            # If the current end is greater than the max_r seen so far,
            # it means this interval is not covered.
            if r > max_r:
                count += 1
                max_r = r
                
        return count