from bisect import bisect_left

class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        # Coordinate compression for Fenwick Tree
        # The prefix sums will range from -n to n
        n = len(nums)
        # Transform: 1 if nums[i] == target else -1
        # Prefix sum array
        pref = [0] * (n + 1)
        for i in range(n):
            val = 1 if nums[i] == target else -1
            pref[i + 1] = pref[i] + val
            
        # Collect all unique prefix sums for coordinate compression
        sorted_pref = sorted(list(set(pref)))
        rank = {val: i + 1 for i, val in enumerate(sorted_pref)}
        
        # Fenwick Tree to count frequencies of prefix sums encountered so far
        bit = [0] * (len(sorted_pref) + 1)
        
        def update(i, delta):
            while i < len(bit):
                bit[i] += delta
                i += i & (-i)
        
        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & (-i)
            return s
        
        count = 0
        for p in pref:
            # We need number of previous pref values < p
            count += query(rank[p] - 1)
            # Add current pref to the bit
            update(rank[p], 1)
            
        return count