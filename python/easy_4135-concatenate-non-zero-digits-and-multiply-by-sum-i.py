class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # Convert to string to easily iterate through digits
        s = str(n)
        
        # Extract only non-zero digits
        non_zero_digits = [int(digit) for digit in s if digit != '0']
        
        # If no non-zero digits were found, return 0
        if not non_zero_digits:
            return 0
            
        # Concatenate them to form x
        # Join the digits as strings, then convert to integer
        x = int("".join(map(str, non_zero_digits)))
        
        # Calculate the sum of the digits in x
        digit_sum = sum(non_zero_digits)
        
        # Return the product
        return x * digit_sum