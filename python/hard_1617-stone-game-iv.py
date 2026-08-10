class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # dp[i] will store whether the current player wins with i stones
        dp = [False] * (n + 1)
        
        for i in range(1, n + 1):
            k = 1
            # Try removing any non-zero square number of stones (1, 4, 9, 16, ...)
            while k * k <= i:
                # If removing k*k stones leaves the opponent in a losing state,
                # then the current player wins from state i.
                if not dp[i - k * k]:
                    dp[i] = True
                    break
                k += 1
                
        return dp[n]