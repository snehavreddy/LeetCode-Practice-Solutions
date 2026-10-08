class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        opened = 0
        
        for char in s:
            if char == '(':
                # If it's > 0, it's not the outermost opening bracket
                if opened > 0:
                    result.append(char)
                opened += 1
            elif char == ')':
                opened -= 1
                # If it's > 0, it's not the outermost closing bracket
                if opened > 0:
                    result.append(char)
                    
        return "".join(result)