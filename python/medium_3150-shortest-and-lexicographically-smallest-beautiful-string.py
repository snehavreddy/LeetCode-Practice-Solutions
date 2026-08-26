class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones_count = 0
        best_str = ""
        
        for right in range(len(s)):
            # Expand the window by adding the right character
            if s[right] == '1':
                ones_count += 1
            
            # When we have exactly 'k' 1s, try to shrink from the left
            while ones_count == k:
                candidate = s[left:right + 1]
                
                # Update the best string if:
                # 1. It's the first one we've found
                # 2. It's shorter than the current best
                # 3. It's the same length but lexicographically smaller
                if not best_str:
                    best_str = candidate
                elif len(candidate) < len(best_str):
                    best_str = candidate
                elif len(candidate) == len(best_str) and candidate < best_str:
                    best_str = candidate
                
                # Shrink the window from the left
                if s[left] == '1':
                    ones_count -= 1
                left += 1
                
        return best_str