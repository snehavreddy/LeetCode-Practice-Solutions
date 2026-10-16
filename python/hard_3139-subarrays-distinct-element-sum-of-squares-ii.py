from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        
        # Segment tree arrays (1-indexed for the tree nodes)
        sum1 = [0] * (4 * n)
        sum2 = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def apply(node, l, r, val):
            val %= MOD
            length = r - l + 1
            # (c + val)^2 = c^2 + 2*c*val + val^2
            sum2[node] = (sum2[node] + 2 * val * sum1[node] + val * val * length) % MOD
            sum1[node] = (sum1[node] + val * length) % MOD
            lazy[node] = (lazy[node] + val) % MOD

        def push_down(node, l, r):
            if lazy[node]:
                mid = (l + r) // 2
                apply(2 * node, l, mid, lazy[node])
                apply(2 * node + 1, mid + 1, r, lazy[node])
                lazy[node] = 0

        def push_up(node):
            sum1[node] = (sum1[2 * node] + sum1[2 * node + 1]) % MOD
            sum2[node] = (sum2[2 * node] + sum2[2 * node + 1]) % MOD

        def update(node, l, r, ql, qr, val):
            if ql <= l and r <= qr:
                apply(node, l, r, val)
                return
            push_down(node, l, r)
            mid = (l + r) // 2
            if ql <= mid:
                update(2 * node, l, mid, ql, qr, val)
            if qr > mid:
                update(2 * node + 1, mid + 1, r, ql, qr, val)
            push_up(node)

        last_pos = {}
        ans = 0
        
        for i in range(n):
            x = nums[i]
            # The range to increment is from the element's last occurrence + 1 to the current index
            start = last_pos.get(x, -1) + 1
            end = i
            
            # Increment counts for all active subarrays in the range
            update(1, 0, n - 1, start, end, 1)
            
            # Add the total sum of squares for all subarrays ending at index i
            ans = (ans + sum2[1]) % MOD
            
            # Record the current element's most recent position
            last_pos[x] = i
            
        return ans