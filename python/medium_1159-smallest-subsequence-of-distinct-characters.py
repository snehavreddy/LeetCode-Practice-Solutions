class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Map each character to its last occurrence index
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        stack = []
        # Keep track of characters already in the stack
        visited = set()
        
        for i, char in enumerate(s):
            # If the character is already in the stack, skip it
            if char in visited:
                continue
            
            # While the stack is not empty, the current char is smaller than 
            # the top of the stack, and the top element appears later in the 
            # string, we can remove the top element to make the result smaller.
            while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                removed_char = stack.pop()
                visited.remove(removed_char)
            
            stack.append(char)
            visited.add(char)
            
        return "".join(stack)