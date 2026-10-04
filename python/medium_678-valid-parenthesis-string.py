class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = 0 # Minimum possible open left parentheses
        cmax = 0 # Maximum possible open left parentheses
        
        for char in s:
            if char == '(':
                cmin += 1
                cmax += 1
            elif char == ')':
                cmin = max(cmin - 1, 0)
                cmax -= 1
            elif char == '*':
                # '*' can be '(', ')', or ''
                cmax += 1              # If '*' is '('
                cmin = max(cmin - 1, 0) # If '*' is ')'
                
            # If at any point the maximum possible open parentheses is negative,
            # it means we have more ')' than '(' and '*' combined.
            if cmax < 0:
                return False
                
        # If cmin is 0, it means we can successfully match all open parentheses.
        return cmin == 0