from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_num = max(nums)
        
        # Count occurrences of each number
        counts = [0] * (max_num + 1)
        for x in nums:
            counts[x] += 1
            
        # gCount[i] will store the number of pairs with GCD exactly i
        gCount = [0] * (max_num + 1)
        
        # Iterate backwards from max_num to 1 to apply inclusion-exclusion
        for i in range(max_num, 0, -1):
            # Find how many numbers are multiples of i
            multiples_count = 0
            for j in range(i, max_num + 1, i):
                multiples_count += counts[j]
            
            # Number of pairs with GCD being a multiple of i
            pairs_with_multiple_i = (multiples_count * (multiples_count - 1)) // 2
            
            # Subtract counts of pairs whose GCD is 2i, 3i, 4i... 
            # to get pairs with GCD exactly i
            for j in range(2 * i, max_num + 1, i):
                pairs_with_multiple_i -= gCount[j]
            
            gCount[i] = pairs_with_multiple_i
            
        # Create a prefix sum of gCount to facilitate binary search
        prefix_sum = [0] * (max_num + 1)
        for i in range(1, max_num + 1):
            prefix_sum[i] = prefix_sum[i-1] + gCount[i]
            
        # Answer each query using binary search on the prefix sum array
        answer = []
        for q in queries:
            # We are looking for the smallest g such that prefix_sum[g] > q
            # bisect_right finds the insertion point to maintain order
            answer.append(bisect_right(prefix_sum, q))
            
        return answer