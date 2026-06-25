class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = 0
        
        # Iterate over all possible starting positions of the subarray
        for i in range(n):
            target_count = 0
            # Iterate over all possible ending positions
            for j in range(i, n):
                if nums[j] == target:
                    target_count += 1
                
                # Check if target is the majority element:
                # Strictly more than half means: 2 * count > length
                length = j - i + 1
                if 2 * target_count > length:
                    count += 1
                    
        return count