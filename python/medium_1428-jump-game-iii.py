class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()

        def dfs(idx):

            # out of bounds or already visited
            if idx < 0 or idx >= len(arr) or idx in visited:
                return False

            # found 0
            if arr[idx] == 0:
                return True

            visited.add(idx)

            return dfs(idx + arr[idx]) or dfs(idx - arr[idx])

        return dfs(start)