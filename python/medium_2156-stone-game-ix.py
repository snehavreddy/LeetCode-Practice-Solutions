class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        # Array to store the frequency of remainders (0, 1, and 2)
        counts = [0, 0, 0]
        
        for stone in stones:
            counts[stone % 3] += 1
            
        # If the number of 0s is even, they essentially cancel out
        if counts[0] % 2 == 0:
            return counts[1] > 0 and counts[2] > 0
        
        # If the number of 0s is odd, the winner parity shifts
        else:
            return abs(counts[1] - counts[2]) > 2