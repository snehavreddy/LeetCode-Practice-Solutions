class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        results = []
        
        # Iterate over all possible starting digits
        for start in range(1, 10):
            num = start
            next_digit = start + 1
            
            # Keep appending the next digit to form a sequential number
            while num <= high and next_digit <= 9:
                num = num * 10 + next_digit
                
                # Check if the generated number is within the range
                if low <= num <= high:
                    results.append(num)
                
                next_digit += 1
        
        # Return the sorted list of results
        return sorted(results)