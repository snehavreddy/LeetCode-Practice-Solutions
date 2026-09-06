class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # dp[j] stores the number of distinct subsequences of s 
        # (up to the current character) that equal the prefix of t of length j.
        dp = [0] * (n + 1)
        
        # An empty string 't' can be formed exactly 1 way from any prefix of 's' (by deleting everything)
        dp[0] = 1 
        
        for i in range(1, m + 1):
            # Traverse j backwards so we use the previous state of dp[j-1] 
            # before it gets updated for the current row i.
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
                    
        return dp[n]