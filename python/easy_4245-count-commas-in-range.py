class Solution:
    def countCommas(self, n: int) -> int:
        # If n is less than 1000, no commas are used.
        # Otherwise, every number from 1000 to n has exactly 1 comma.
        return max(0, n - 999)