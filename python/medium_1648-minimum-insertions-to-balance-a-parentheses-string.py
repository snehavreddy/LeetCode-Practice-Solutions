class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        req_right = 0
        
        for char in s:
            if char == '(':
                # If we have an odd number of required right parentheses (meaning 
                # there's a pending ')' needed for a previous '('), we must balance
                # it before opening a new '(' by inserting one ')'.
                if req_right % 2 != 0:
                    insertions += 1
                    req_right -= 1
                
                # Every new '(' requires two '))'
                req_right += 2
            else:
                # We encounter a ')'
                req_right -= 1
                
                # If required right parentheses drops below 0, it means we have a ')' 
                # without a matching '('. We must insert one '('.
                if req_right < 0:
                    insertions += 1
                    # Since we virtually inserted a '(', it requires two ')'. 
                    # We just used one ')' to trigger this, so we still need 1 more ')'.
                    req_right += 2
                    
        # Add any unmatched required right parentheses to the total insertions
        return insertions + req_right