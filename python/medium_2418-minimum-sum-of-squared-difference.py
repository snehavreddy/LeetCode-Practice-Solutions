class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        
        # Max difference according to constraints is 10^5
        diff_counts = [0] * 100001
        max_diff = 0
        
        # Count the frequency of each absolute difference
        for a, b in zip(nums1, nums2):
            d = abs(a - b)
            diff_counts[d] += 1
            if d > max_diff:
                max_diff = d
                
        # Greedily reduce the largest differences
        for i in range(max_diff, 0, -1):
            if diff_counts[i] > 0:
                if k == 0:
                    break
                
                # We can at most reduce 'k' elements or all elements with difference 'i'
                reduce_amount = min(diff_counts[i], k)
                
                diff_counts[i] -= reduce_amount
                diff_counts[i - 1] += reduce_amount
                k -= reduce_amount
                
        # Calculate the final sum of squared differences
        ans = 0
        for i in range(1, max_diff + 1):
            if diff_counts[i] > 0:
                ans += diff_counts[i] * (i * i)
                
        return ans