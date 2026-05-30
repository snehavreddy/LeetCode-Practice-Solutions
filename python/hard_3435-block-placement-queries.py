class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        
    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])
        
    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        return max(self.query(2 * node, start, mid, l, r),
                   self.query(2 * node + 1, mid + 1, end, l, r))

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        # Limit based on constraints
        limit = 50000
        st = SegmentTree(limit)
        
        # Use a sorted list or maintain obstacles to find neighbors
        # For simplicity and efficiency in Python:
        import bisect
        obstacles = [0, limit]
        
        results = []
        
        for q in queries:
            if q[0] == 1:
                x = q[1]
                idx = bisect.bisect_left(obstacles, x)
                prev_x = obstacles[idx - 1]
                next_x = obstacles[idx]
                
                # Update the gaps in the segment tree
                # The old gap (next_x - prev_x) is replaced by two new ones
                st.update(1, 0, limit, x, x - prev_x)
                st.update(1, 0, limit, next_x, next_x - x)
                
                bisect.insort(obstacles, x)
                
            else:
                x, sz = q[1], q[2]
                idx = bisect.bisect_right(obstacles, x)
                prev_x = obstacles[idx - 1]
                
                # Check the gap between last obstacle and x, 
                # then check max gap in range [0, prev_x]
                max_gap = max(x - prev_x, st.query(1, 0, limit, 0, prev_x))
                
                results.append(max_gap >= sz)
                
        return results