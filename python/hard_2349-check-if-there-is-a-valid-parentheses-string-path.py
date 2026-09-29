from functools import cache

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # A valid parentheses string must have an even length
        # The length of any path in this grid is m + n - 1
        if (m + n - 1) % 2 != 0:
            return False
            
        # A valid path cannot start with a closing parenthesis 
        # or end with an opening parenthesis
        if grid[0][0] == ')' or grid[-1][-1] == '(':
            return False

        @cache
        def dfs(r, c, balance):
            if grid[r][c] == '(':
                balance += 1
            else:
                balance -= 1
                
            # Balance cannot be negative at any point
            if balance < 0:
                return False
                
            # If we reached the bottom-right corner, check if balance is exactly 0
            if r == m - 1 and c == n - 1:
                return balance == 0
            
            res = False
            # Move down
            if r + 1 < m:
                res = res or dfs(r + 1, c, balance)
            # Move right
            if c + 1 < n:
                res = res or dfs(r, c + 1, balance)
                
            return res

        return dfs(0, 0, 0)