class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        
        # Calculate suffix sums to quickly find the total sum of remaining piles
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        # dp[i][M] stores the maximum stones a player can get starting from index i with parameter M
        dp = {}

        def get_max_stones(i: int, m: int) -> int:
            # If remaining piles can all be taken, take all of them
            if i + 2 * m >= n:
                return suffix_sum[i]
            
            if (i, m) in dp:
                return dp[(i, m)]
            
            # The current player minimizes the maximum stones the opponent can get in their turn
            min_opponent_stones = float('inf')
            for x in range(1, 2 * m + 1):
                min_opponent_stones = min(min_opponent_stones, get_max_stones(i + x, max(m, x)))
            
            # Maximum stones current player can get = (Total remaining) - (Opponent's max score)
            dp[(i, m)] = suffix_sum[i] - min_opponent_stones
            return dp[(i, m)]

        return get_max_stones(0, 1)