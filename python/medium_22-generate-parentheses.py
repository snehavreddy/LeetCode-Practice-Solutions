class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        def backtrack(open_count, close_count, current_string):
            # Base case: if we have used all n opening and closing parentheses
            if open_count == close_count == n:
                res.append(current_string)
                return
            
            # If we can still add an opening parenthesis, add it
            if open_count < n:
                backtrack(open_count + 1, close_count, current_string + "(")
                
            # If we have more opening than closing, we can safely add a closing parenthesis
            if close_count < open_count:
                backtrack(open_count, close_count + 1, current_string + ")")
                
        backtrack(0, 0, "")
        return res