class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        last_used = -1  # Tracks the end index of the last selected palindrome
        
        for i in range(k - 1, n):
            # 1. Check if there is a palindrome of exactly length `k` ending at `i`
            start_k = i - k + 1
            if start_k > last_used:
                t1 = s[start_k : i + 1]
                if t1 == t1[::-1]:
                    ans += 1
                    last_used = i
                    continue # Found the shortest valid palindrome, no need to check k+1
            
            # 2. Check if there is a palindrome of exactly length `k + 1` ending at `i`
            start_k_plus_1 = i - k
            if start_k_plus_1 > last_used:
                t2 = s[start_k_plus_1 : i + 1]
                if t2 == t2[::-1]:
                    ans += 1
                    last_used = i
                    
        return ans