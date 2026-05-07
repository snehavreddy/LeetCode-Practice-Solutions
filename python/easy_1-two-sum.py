class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in visited:
                return [visited[diff], i]
            visited[nums[i]] = i
            
        return []