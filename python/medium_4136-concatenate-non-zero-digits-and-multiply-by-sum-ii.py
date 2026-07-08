class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)
        
        # Store non-zero digits and their original indices
        nz_digits = []
        for i, char in enumerate(s):
            if char != '0':
                nz_digits.append((i, int(char)))
        
        m = len(nz_digits)
        if m == 0:
            return [0] * len(queries)
            
        # Prefix sums of non-zero digits
        pref_sum = [0] * (m + 1)
        for i in range(m):
            pref_sum[i+1] = (pref_sum[i] + nz_digits[i][1]) % MOD
            
        # Prefix concatenation values and powers of 10
        # P[i] stores the value of the first i digits concatenated
        P = [0] * (m + 1)
        pow10 = [1] * (m + 1)
        for i in range(m):
            P[i+1] = (P[i] * 10 + nz_digits[i][1]) % MOD
            pow10[i+1] = (pow10[i] * 10) % MOD
            
        # Map original indices to index in nz_digits for binary search
        indices = [d[0] for d in nz_digits]
        
        results = []
        for l, r in queries:
            # Find range [idx_l, idx_r] in nz_digits
            import bisect
            idx_l = bisect.bisect_left(indices, l)
            idx_r = bisect.bisect_right(indices, r) - 1
            
            if idx_l > idx_r:
                results.append(0)
            else:
                # Sum of digits
                s_val = (pref_sum[idx_r + 1] - pref_sum[idx_l]) % MOD
                
                # Concatenated integer x: P[idx_r+1] - P[idx_l] * 10^(number of digits)
                length = idx_r - idx_l + 1
                x = (P[idx_r + 1] - P[idx_l] * pow10[length]) % MOD
                
                results.append((x * s_val) % MOD)
                
        return results