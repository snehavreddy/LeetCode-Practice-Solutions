from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        # best_len_until[i] stores the minimum length of a valid sub-array ending at or before index i
        best_len_until = [float('inf')] * n
        min_len = float('inf') # Tracks the minimum length seen so far
        ans = float('inf')     # Tracks the best sum of two sub-array lengths
        
        left = 0
        current_sum = 0
        
        for right in range(n):
            current_sum += arr[right]
            
            # Shrink the window from the left if the sum exceeds the target
            while current_sum > target and left <= right:
                current_sum -= arr[left]
                left += 1
                
            # If we found a valid sub-array
            if current_sum == target:
                curr_len = right - left + 1
                
                # If there is a valid non-overlapping sub-array before the current one
                if left > 0 and best_len_until[left - 1] != float('inf'):
                    ans = min(ans, curr_len + best_len_until[left - 1])
                
                # Update the minimum length found so far
                min_len = min(min_len, curr_len)
                
            # Store the best length found up to the current index
            best_len_until[right] = min_len
            
        return ans if ans != float('inf') else -1