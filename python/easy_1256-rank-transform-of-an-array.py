class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # 1. Create a sorted list of unique elements
        sorted_unique = sorted(list(set(arr)))
        
        # 2. Create a rank map: number -> rank
        rank_map = {val: i + 1 for i, val in enumerate(sorted_unique)}
        
        # 3. Build the result array by looking up each element in the map
        return [rank_map[x] for x in arr]