class Solution:
    def maxDistance(self, side: int, points: list[list[int]], k: int) -> int:
        # Convert to 1D perimeter distance (clockwise from origin)
        def to_perimeter(x, y):
            if y == 0:
                return x
            elif x == side:
                return side + y
            elif y == side:
                return 2 * side + (side - x)
            else:
                return 3 * side + (side - y)
        
        n = len(points)
        perimeter = 4 * side
        pos = sorted(to_perimeter(x, y) for x, y in points)
        
        # Check if we can place k points with min distance >= d
        def can_place(d):
            # Try each starting point
            for start in range(n):
                count = 1
                curr = pos[start]
                idx = start
                
                for _ in range(k - 1):
                    # Binary search for next point >= curr + d
                    target = curr + d
                    
                    # Search in [idx+1, start+n) with wraparound
                    lo, hi = idx + 1, start + n
                    while lo < hi:
                        mid_idx = (lo + hi) // 2
                        p = pos[mid_idx % n]
                        # Handle wraparound
                        if mid_idx >= n and mid_idx % n <= start:
                            p += perimeter
                        if p >= target:
                            hi = mid_idx
                        else:
                            lo = mid_idx + 1
                    
                    if lo >= start + n:
                        break
                    
                    idx = lo
                    curr = pos[idx % n]
                    if idx >= n:
                        curr += perimeter
                    count += 1
                
                # Check circular distance from last to first
                if count == k:
                    last_pos = curr
                    first_pos = pos[start] + perimeter
                    if first_pos - last_pos >= d:
                        return True
            
            return False
        
        # Binary search on the answer
        lo, hi = 1, perimeter // k
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_place(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return ans
