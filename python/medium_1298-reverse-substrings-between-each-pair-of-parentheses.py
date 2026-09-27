class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        curr = []
        
        for char in s:
            if char == '(':
                # Push the current string to the stack and start a new one
                stack.append(curr)
                curr = []
            elif char == ')':
                # Reverse the current string
                curr.reverse()
                # Append the reversed string to the last string waiting in the stack
                curr = stack.pop() + curr
            else:
                # Add normal characters to the current string
                curr.append(char)
                
        return "".join(curr)