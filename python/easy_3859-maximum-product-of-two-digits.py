class Solution:

  def maxProduct(self, n: int) -> int:
    # Convert the number to a string of its digits, then to a list of integers
    digits = [int(ch) for ch in str(n)]
    # Sort the digits in ascending order
    digits.sort()
    # Return the product of the two largest digits (the last two elements)
    return digits[-1] * digits[-2]