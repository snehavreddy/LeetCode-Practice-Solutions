import math

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        # The number of ways is simply (n + k - 1) choose (2 * k)
        ans = math.comb(n + k - 1, 2 * k)
        
        return ans % MOD