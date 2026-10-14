class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # If the required sum is greater than the maximum possible sum we can get
        # with 'num' digits (which is all 9s), it's impossible.
        if sum > 9 * num:
            return ""
        
        # Calculate how many 9s we can use
        nines = sum // 9
        remainder = sum % 9
        
        # Build the result string
        ans = "9" * nines
        if remainder > 0:
            ans += str(remainder)
            
        # Pad the rest of the string with 0s to make its length exactly 'num'
        zeros = num - len(ans)
        ans += "0" * zeros
        
        return ans