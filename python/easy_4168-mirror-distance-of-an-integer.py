class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev = self.reverse(n)
        return abs(n - rev)

    def reverse(self, n: int) -> int:
        rev = 0
        while n > 0:
            digit = n % 10
            rev = rev * 10 + digit
            n //= 10
        return rev
