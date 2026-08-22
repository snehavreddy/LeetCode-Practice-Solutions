class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_prod = 1
        
        # Iterate through each digit of the number
        for digit_str in str(n):
            digit = int(digit_str)
            digit_sum += digit
            digit_prod *= digit
            
        # Check if n is divisible by the sum of its digit sum and digit product
        return n % (digit_sum + digit_prod) == 0