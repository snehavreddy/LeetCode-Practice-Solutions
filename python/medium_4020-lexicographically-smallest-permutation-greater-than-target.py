from collections import Counter
import string

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        # Keep track of available characters from s
        rem = Counter(s)
        
        # best_k will store the maximum length of prefix we can match
        # before diverging with a character strictly greater than target's
        best_k = -1
        best_ch = ''
        
        n = len(s)
        
        for i in range(n):
            # Try to find the smallest available character that is strictly greater than target[i]
            cand_ch = None
            for ch in string.ascii_lowercase:
                if ch > target[i] and rem[ch] > 0:
                    cand_ch = ch
                    break # since we check alphabetically, the first found is the smallest
            
            # If we found one, record this divergence point
            if cand_ch:
                best_k = i
                best_ch = cand_ch
            
            # Now, attempt to match target[i] to continue extending the prefix
            if rem[target[i]] > 0:
                rem[target[i]] -= 1
            else:
                # Can't match target[i], so we can't extend the prefix any further
                break
                
        # If no valid divergence point was found, it's impossible to form a greater string
        if best_k == -1:
            return ""
        
        # Reconstruct the optimal string
        # 1. Prefix exactly matches target up to best_k
        ans = list(target[:best_k])
        
        # 2. Add the divergence character
        ans.append(best_ch)
        
        # 3. Add the rest of the available characters sorted alphabetically
        used = Counter(ans)
        original = Counter(s)
        
        remaining_chars = []
        for ch in string.ascii_lowercase:
            count = original[ch] - used[ch]
            if count > 0:
                remaining_chars.extend([ch] * count)
                
        ans.extend(remaining_chars)
        
        return "".join(ans)