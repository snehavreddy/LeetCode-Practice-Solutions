class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Mapping of closing brackets to their corresponding opening brackets
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value '#' to top_element
                top_element = stack.pop() if stack else '#'
                
                # If the mapping for this bracket doesn't match the stack's top element, return false.
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)
                
        # In the end, if the stack is empty, then we have a valid expression.
        return not stack