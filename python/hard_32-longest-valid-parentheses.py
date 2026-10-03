class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        # Initialize stack with -1 to serve as the base index for valid substrings
        stack = [-1]
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # If stack is empty, this ')' is unmatched and acts as a new base
                    stack.append(i)
                else:
                    # Calculate the length of the current valid substring
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len