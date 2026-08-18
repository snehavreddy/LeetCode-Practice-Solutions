class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        
        # Dictionary to count the number of subarrays each integer appears in
        appearance_counts = defaultdict(int)
        n = len(nums)
        
        # Iterate over every starting index of a subarray of size k
        for i in range(n - k + 1):
            # Extract the subarray
            subarray = nums[i : i + k]
            
            # Add unique elements of this subarray to our counts
            # We use set() because we only care IF the number appears in the subarray, 
            # not how many times it appears within this specific subarray.
            for num in set(subarray):
                appearance_counts[num] += 1
                
        # Find the maximum integer that appears in exactly 1 subarray
        max_almost_missing = -1
        for num, count in appearance_counts.items():
            if count == 1:
                max_almost_missing = max(max_almost_missing, num)
                
        return max_almost_missing