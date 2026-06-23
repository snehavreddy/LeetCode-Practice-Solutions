class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        M = r - l + 1
        
        # Initial state for length 2
        # dp0[v]: count ending in v, last step decreasing (prev > v)
        # dp1[v]: count ending in v, last step increasing (prev < v)
        dp0 = [M - 1 - v for v in range(M)]
        dp1 = [v for v in range(M)]
        
        for _ in range(3, n + 1):
            new_dp0 = [0] * M
            new_dp1 = [0] * M
            
            # Use running totals to calculate sums in O(1)
            # s0 tracks the sum of dp0 values we've seen so far (for next increasing steps)
            # s1 tracks the sum of remaining dp1 values (for next decreasing steps)
            s0 = 0
            s1 = sum(dp1)
            
            for v in range(M):
                # To form a decreasing step (prev > v), we need sum of dp1 where prev > v
                # We subtract dp1[v] from s1 as we move to the next index
                s1 -= dp1[v]
                new_dp0[v] = s1 % MOD
                
                # To form an increasing step (prev < v), we need sum of dp0 where prev < v
                # s0 already contains the sum of dp0[0...v-1]
                new_dp1[v] = s0
                s0 = (s0 + dp0[v]) % MOD
                
            dp0, dp1 = new_dp0, new_dp1
            
        return sum(dp0[v] + dp1[v] for v in range(M)) % MOD