class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        # Initialize arr1 and arr2 with the first two elements
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        
        # Iterate through the rest of the elements
        for i in range(2, len(nums)):
            # Compare the last elements of arr1 and arr2
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
                
        # Concatenate and return the result
        return arr1 + arr2