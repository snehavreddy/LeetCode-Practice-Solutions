from typing import List
import collections

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Map to store reserved seats for each row (only storing relevant seats 2-9)
        reserved_map = collections.defaultdict(set)
        
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                reserved_map[row].add(seat)
                
        # Calculate groups for completely empty rows
        # Each empty row can accommodate exactly 2 groups
        max_groups = (n - len(reserved_map)) * 2
        
        # Calculate groups for rows with reservations
        for seats in reserved_map.values():
            left_available = not any(s in seats for s in (2, 3, 4, 5))
            right_available = not any(s in seats for s in (6, 7, 8, 9))
            middle_available = not any(s in seats for s in (4, 5, 6, 7))
            
            if left_available and right_available:
                max_groups += 2
            elif left_available or right_available or middle_available:
                max_groups += 1
                
        return max_groups