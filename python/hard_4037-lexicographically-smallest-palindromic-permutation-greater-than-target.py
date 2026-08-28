class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        # Count the frequency of each character in s
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1
            
        # Determine the center character for odd-length strings
        center = ""
        for i in range(26):
            if freq[i] % 2 != 0:
                if center != "": 
                    return ""  # A palindrome cannot have more than one odd-frequency character
                center = chr(ord('a') + i)
                freq[i] -= 1
                
        sz = len(s)
        half = sz // 2
        
        # Helper function to check if we have enough characters
        def check(f):
            return all(count >= 0 for count in f)
        
        # 1. Try to exactly match the first half of the target string
        for i in range(half):
            freq[ord(target[i]) - ord('a')] -= 2
            
        if check(freq):
            head = target[:half]
            rev = head[::-1]
            tail = center + rev if center != "" else rev
            
            # Check if the resulting palindrome is strictly greater than the target
            if tail > target[half:]:
                return head + tail
                
        # 2. Backtrack from right to left to find the next lexicographically larger valid first half
        for i in range(half - 1, -1, -1):
            w = target[i]
            # Restore the character we are replacing
            freq[ord(w) - ord('a')] += 2
            
            if not check(freq):
                continue
                
            # Try to place the next available character that is strictly greater than target[i]
            for j in range(ord(w) - ord('a') + 1, 26):
                if freq[j] == 0:
                    continue
                    
                freq[j] -= 2
                
                # Construct the new prefix head
                result_head = list(target[:i])
                result_head.append(chr(ord('a') + j))
                
                # Fill the rest of the first half with the smallest available characters in ascending order
                for k in range(26):
                    cnt = freq[k] // 2
                    if cnt > 0:
                        result_head.extend([chr(ord('a') + k)] * cnt)
                        
                head = "".join(result_head)
                part = head[::-1]
                
                # Mirror to create the full palindrome string
                res = head
                if center != "":
                    res += center
                res += part
                
                return res
                
        return ""