class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        
        # Segment tree arrays
        tree_prod = [0] * (4 * n)
        tree_counts = [[0] * k for _ in range(4 * n)]
        
        def build(node, l, r):
            if l == r:
                v_mod = nums[l] % k
                tree_prod[node] = v_mod
                tree_counts[node][v_mod] = 1
                return
            
            mid = (l + r) // 2
            left = 2 * node + 1
            right = 2 * node + 2
            
            build(left, l, mid)
            build(right, mid + 1, r)
            
            # Merge logic
            tree_prod[node] = (tree_prod[left] * tree_prod[right]) % k
            for i in range(k):
                tree_counts[node][i] = tree_counts[left][i]
            for i in range(k):
                if tree_counts[right][i] > 0:
                    nv = (tree_prod[left] * i) % k
                    tree_counts[node][nv] += tree_counts[right][i]

        def update(node, l, r, idx, val):
            if l == r:
                v_mod = val % k
                tree_prod[node] = v_mod
                for i in range(k):
                    tree_counts[node][i] = 0
                tree_counts[node][v_mod] = 1
                return
            
            mid = (l + r) // 2
            left = 2 * node + 1
            right = 2 * node + 2
            
            if idx <= mid:
                update(left, l, mid, idx, val)
            else:
                update(right, mid + 1, r, idx, val)
                
            # Merge logic
            tree_prod[node] = (tree_prod[left] * tree_prod[right]) % k
            for i in range(k):
                tree_counts[node][i] = tree_counts[left][i]
            for i in range(k):
                if tree_counts[right][i] > 0:
                    nv = (tree_prod[left] * i) % k
                    tree_counts[node][nv] += tree_counts[right][i]

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree_prod[node], tree_counts[node]
                
            mid = (l + r) // 2
            if qr <= mid:
                return query(2 * node + 1, l, mid, ql, qr)
            if ql > mid:
                return query(2 * node + 2, mid + 1, r, ql, qr)
                
            # If the query range overlaps both halves
            prod1, counts1 = query(2 * node + 1, l, mid, ql, qr)
            prod2, counts2 = query(2 * node + 2, mid + 1, r, ql, qr)
            
            new_counts = list(counts1)
            for v in range(k):
                if counts2[v] > 0:
                    nv = (prod1 * v) % k
                    new_counts[nv] += counts2[v]
                    
            return (prod1 * prod2) % k, new_counts

        # Build the initial segment tree
        build(0, 0, n - 1)
        
        result = []
        for index, value, start, x in queries:
            # Step 1: Update nums[index] to value
            update(0, 0, n - 1, index, value)
            
            # Step 2: Query for the frequency of remainder x in the range [start, n - 1]
            _, counts = query(0, 0, n - 1, start, n - 1)
            result.append(counts[x])
            
        return result