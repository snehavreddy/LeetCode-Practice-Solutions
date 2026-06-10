import heapq
import math

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # 1. Build Sparse Tables for O(1) Range Max/Min Queries
        log_n = n.bit_length()
        st_max = [[0] * n for _ in range(log_n)]
        st_min = [[0] * n for _ in range(log_n)]
        
        for i in range(n):
            st_max[0][i] = nums[i]
            st_min[0][i] = nums[i]
            
        for j in range(1, log_n):
            for i in range(n - (1 << j) + 1):
                st_max[j][i] = max(st_max[j-1][i], st_max[j-1][i + (1 << (j-1))])
                st_min[j][i] = min(st_min[j-1][i], st_min[j-1][i + (1 << (j-1))])
                
        def query(l, r):
            j = (r - l + 1).bit_length() - 1
            mx = max(st_max[j][l], st_max[j][r - (1 << j) + 1])
            mn = min(st_min[j][l], st_min[j][r - (1 << j) + 1])
            return mx - mn

        # 2. Use Max-Heap to greedily pick the top k values
        # Heap stores: (-value, l, r)
        pq = []
        for l in range(n):
            val = query(l, n - 1)
            heapq.heappush(pq, (-val, l, n - 1))
            
        total_value = 0
        for _ in range(k):
            neg_val, l, r = heapq.heappop(pq)
            total_value += (-neg_val)
            
            # Push the next subarray for this start index l: [l, r-1]
            if r > l:
                new_val = query(l, r - 1)
                heapq.heappush(pq, (-new_val, l, r - 1))
                
        return total_value