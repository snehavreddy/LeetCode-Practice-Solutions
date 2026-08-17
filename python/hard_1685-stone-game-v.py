from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        sz = len(stoneValue)
        
        # dp[i][j] stores the max score Alice can get from stones i to j
        # maxScore stores the running maximums to avoid O(N) inner loops
        dp = [[0] * sz for _ in range(sz)]
        maxScore = [[0] * sz for _ in range(sz)]
        
        # Base cases: sub-arrays of length 1
        for i in range(sz):
            maxScore[i][i] = stoneValue[i]
            
        # Iterate over the right endpoint j
        for j in range(1, sz):
            # mid tracks the split point where left_sum >= right_sum
            mid = j 
            sm = stoneValue[j] # sm keeps track of the total sum of stones[i...j]
            rightHalf = 0      # Sum of stones[mid...j]
            
            # Expand the window to the left
            for i in range(j - 1, -1, -1):
                sm += stoneValue[i]
                
                # Shift mid leftwards as long as left half is strictly less than right half
                # (represented here as rightHalf * 2 > sm)
                while (rightHalf + stoneValue[mid]) * 2 <= sm:
                    rightHalf += stoneValue[mid]
                    mid -= 1
                    
                # Calculate dp[i][j] based on the found mid point
                # 1. If left and right halves are exactly equal, Alice gets the max of both sides
                if rightHalf * 2 == sm:
                    dp[i][j] = maxScore[i][mid]
                # 2. Otherwise, she takes the smaller side (left half)
                else:
                    dp[i][j] = 0 if mid == i else maxScore[i][mid - 1]
                    
                # 3. Consider the right side if Bob decides to throw away the left half
                dp[i][j] = max(dp[i][j], 0 if mid == j else maxScore[j][mid + 1])
                
                # Update maxScore for future DP states
                # Upper triangle maxScore[i][j] tracks max of (dp[i][k] + sum) for left partitions
                maxScore[i][j] = max(maxScore[i][j - 1], dp[i][j] + sm)
                
                # Lower triangle maxScore[j][i] tracks max of (dp[k][j] + sum) for right partitions
                maxScore[j][i] = max(maxScore[j][i + 1], dp[i][j] + sm)
                
        return dp[0][sz - 1]