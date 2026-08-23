class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        sumL = sumR = qL = qR = 0
        
        # Calculate sums and count '?' for both halves
        for i in range(n):
            if i < n // 2:
                if num[i] == '?':
                    qL += 1
                else:
                    sumL += int(num[i])
            else:
                if num[i] == '?':
                    qR += 1
                else:
                    sumR += int(num[i])
                    
        # Case 1: If there's an odd number of '?' overall, Alice gets the last move and wins.
        if (qL + qR) % 2 != 0:
            return True
            
        # Case 2: Even number of '?'. Bob wins only if he can exactly balance the sides.
        # This requires: 2 * (sumL - sumR) == 9 * (qR - qL)
        # If it doesn't match, Alice wins.
        return 2 * (sumL - sumR) != 9 * (qR - qL)