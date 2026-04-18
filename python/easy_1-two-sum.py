class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       map_index = {}
       for i in range(len(nums)):
            diff = target - nums[i]
            if diff in map_index:
                return [map_index[diff], i]
            map_index[nums[i]] = i
       return []   
        