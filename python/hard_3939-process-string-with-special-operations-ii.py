class Solution:
    def processStr(self, s: str, k: int) -> str:
        # Forward pass to track string length
        m = 0
        for c in s:
            if c == "*":
                m = max(0, m - 1)
            elif c == "#":
                m <<= 1
            elif c != "%":
                m += 1
        
        # If k is out of bounds
        if k >= m:
            return "."
            
        # Backward pass to find the k-th character
        # Working backwards from the final length m
        for c in reversed(s):
            if c == "*":
                m += 1
            elif c == "#":
                m //= 2
                if k >= m:
                    k -= m
            elif c == "%":
                k = m - 1 - k
            else:
                m -= 1
                if k == m:
                    return c
        return "."