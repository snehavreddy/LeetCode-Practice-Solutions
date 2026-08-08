class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        
        # dp[i] stores the length of the longest suffix of word2 
        # that can be matched starting at or after index i in word1.
        dp = [0] * (n + 1)
        match_len = 0
        for i in range(n - 1, -1, -1):
            if match_len < m and word1[i] == word2[m - 1 - match_len]:
                match_len += 1
            dp[i] = match_len
            
        res = []
        j = 0  # pointer for word2
        used_change = False
        
        for i in range(n):
            if j == m:
                break
                
            if word1[i] == word2[j]:
                res.append(i)
                j += 1
            elif not used_change and j + 1 < m and dp[i + 1] >= m - (j + 1):
                # Use our one allowed replacement/change here
                res.append(i)
                used_change = True
                j += 1
            elif not used_change and j + 1 == m:
                # If we only need 1 more character to finish word2
                res.append(i)
                used_change = True
                j += 1
                
        return res if j == m else []