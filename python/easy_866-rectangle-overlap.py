from typing import List

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # Check if rec1 is completely to the left, right, below, or above rec2
        # rec1[0] = x1, rec1[1] = y1 (bottom-left)
        # rec1[2] = x2, rec1[3] = y2 (top-right)
        
        is_left = rec1[2] <= rec2[0]
        is_right = rec1[0] >= rec2[2]
        is_below = rec1[3] <= rec2[1]
        is_above = rec1[1] >= rec2[3]
        
        # If any of these are true, they do not overlap
        if is_left or is_right or is_below or is_above:
            return False
            
        return True