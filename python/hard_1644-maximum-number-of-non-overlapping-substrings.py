class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Step 1: Find the first and last occurrence of each character
        first = {}
        last = {}
        
        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
            last[char] = i
            
        valid_intervals = []
        
        # Step 2: Find all valid intervals
        for char in set(s):
            left = first[char]
            right = last[char]
            valid = True
            
            i = left
            while i <= right:
                # If a character inside our current range first appears before `left`, 
                # this substring would need to extend to the left. We can mark it invalid 
                # because the optimal valid substring covering it will be discovered 
                # when we evaluate that earlier character.
                if first[s[i]] < left:
                    valid = False
                    break
                # Expand the right boundary if necessary
                right = max(right, last[s[i]])
                i += 1
            
            if valid:
                valid_intervals.append((left, right))
                
        # Step 3: Greedily pick intervals (Interval Scheduling)
        # Sort primarily by end point ascending (to maximize the number of non-overlapping substrings)
        # Secondary sort by start point descending (to pick the shortest interval when endpoints match)
        valid_intervals.sort(key=lambda x: (x[1], -x[0]))
        
        res = []
        last_end = -1
        
        for left, right in valid_intervals:
            if left > last_end:
                res.append(s[left:right+1])
                last_end = right
                
        return res