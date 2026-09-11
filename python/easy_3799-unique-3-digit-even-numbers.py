from typing import List
from itertools import permutations

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        valid_numbers = set()
        
        # Generate all permutations of length 3 from the given digits
        for p in permutations(digits, 3):
            # Check for no leading zero (p[0] != 0) 
            # and if the number is even (p[2] % 2 == 0)
            if p[0] != 0 and p[2] % 2 == 0:
                valid_numbers.add(p)
                
        # Return the count of unique valid numbers
        return len(valid_numbers)