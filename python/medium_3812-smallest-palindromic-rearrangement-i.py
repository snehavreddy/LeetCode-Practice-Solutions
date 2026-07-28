from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)
        left_half = []
        mid_char = ""
        
        # Iterate from 'a' to 'z' to ensure lexicographically smallest order
        for char in sorted(count.keys()):
            freq = count[char]
            # Take half of the characters for the left side
            left_half.append(char * (freq // 2))
            # If the frequency is odd, it must sit in the middle
            if freq % 2 == 1:
                mid_char = char
                
        left_str = "".join(left_half)
        # Combine left half, middle character, and the reverse of left half
        return left_str + mid_char + left_str[::-1]