import math
from typing import List

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        dp = [[0] * 201 for _ in range(201)]
        dp[0][0] = 1

        for x in nums:
            new_dp = [row[:] for row in dp]

            for g1 in range(201):
                for g2 in range(201):
                    if dp[g1][g2] == 0:
                        continue

                    val = dp[g1][g2]

                    ng1 = x if g1 == 0 else math.gcd(g1, x)
                    new_dp[ng1][g2] = (new_dp[ng1][g2] + val) % MOD

                    ng2 = x if g2 == 0 else math.gcd(g2, x)
                    new_dp[g1][ng2] = (new_dp[g1][ng2] + val) % MOD

            dp = new_dp

        ans = 0
        for g in range(1, 201):
            ans = (ans + dp[g][g]) % MOD

        return ans