class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((123 - ord(char)) * (i + 1) for i, char in enumerate(s))