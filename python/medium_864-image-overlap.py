import collections
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        # Lists to store the coordinates of all 1s in both images
        ones_img1 = []
        ones_img2 = []
        
        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    ones_img1.append((r, c))
                if img2[r][c] == 1:
                    ones_img2.append((r, c))
                    
        # If either image has no 1s, there can be no overlap
        if not ones_img1 or not ones_img2:
            return 0
            
        # Dictionary to store the frequencies of each translation vector (dx, dy)
        translation_counts = collections.defaultdict(int)
        max_overlap = 0
        
        # Compare every 1 in img1 with every 1 in img2
        for r1, c1 in ones_img1:
            for r2, c2 in ones_img2:
                # The required translation to move (r1, c1) to (r2, c2)
                vec = (r2 - r1, c2 - c1)
                translation_counts[vec] += 1
                
                # Keep track of the maximum overlap found so far
                if translation_counts[vec] > max_overlap:
                    max_overlap = translation_counts[vec]
                    
        return max_overlap