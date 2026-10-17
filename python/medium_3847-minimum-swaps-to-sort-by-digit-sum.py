class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # Helper function to compute the digit sum (math approach is faster than string conversion)
        def get_digit_sum(n: int) -> int:
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total
        
        n = len(nums)
        # Create an array of tuples: (digit_sum, value, original_index)
        arr = [(get_digit_sum(nums[i]), nums[i], i) for i in range(n)]
        
        # Sort based on digit sum; Python's tuple sort automatically uses the value as a tiebreaker
        arr.sort()
        
        # Visited array to keep track of elements during cycle detection
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            # If already visited or already in the correct position, skip
            if visited[i] or arr[i][2] == i:
                continue
                
            # Find the size of the cycle
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = arr[j][2]
                cycle_size += 1
                
            # If the cycle has more than 1 element, add (cycle_size - 1) to swaps
            if cycle_size > 1:
                swaps += cycle_size - 1
                
        return swaps