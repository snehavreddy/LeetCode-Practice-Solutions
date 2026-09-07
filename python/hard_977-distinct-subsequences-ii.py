class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        
        # Array to store the number of distinct subsequences ending with each character
        end = [0] * 26 
        
        # This keeps track of the total number of distinct subsequences formed so far
        current_sum = 0 
        
        for c in s:
            idx = ord(c) - ord('a')
            
            # The new subsequences we can form are all the previous ones + the character itself.
            # We subtract the ones previously ending with this character to avoid counting duplicates.
            added = (current_sum + 1 - end[idx]) % MOD
            
            # Update the counts
            end[idx] = (end[idx] + added) % MOD
            current_sum = (current_sum + added) % MOD
            
        return current_sum