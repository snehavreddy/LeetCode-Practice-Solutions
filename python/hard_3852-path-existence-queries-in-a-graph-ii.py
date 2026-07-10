class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # 1. Sort indices by value
        sorted_indices = sorted(range(n), key=lambda i: nums[i])
        rank = [0] * n
        for r, i in enumerate(sorted_indices):
            rank[i] = r
            
        # 2. Find range [L, R] reachable in one jump
        # R[i] is the furthest right index reachable from i
        # L[i] is the furthest left index reachable from i
        L = [0] * n
        R = [0] * n
        
        left = 0
        for i in range(n):
            while nums[sorted_indices[i]] - nums[sorted_indices[left]] > maxDiff:
                left += 1
            L[i] = left
            
        right = 0
        for i in range(n):
            while right < n and nums[sorted_indices[right]] - nums[sorted_indices[i]] <= maxDiff:
                right += 1
            R[i] = right - 1

        # 3. Build Sparse Tables (Binary Lifting)
        LOG = n.bit_length()
        up = [[R[i] for i in range(n)] for _ in range(LOG)]
        down = [[L[i] for i in range(n)] for _ in range(LOG)]
        
        for k in range(1, LOG):
            for i in range(n):
                up[k][i] = up[k-1][up[k-1][i]]
                down[k][i] = down[k-1][down[k-1][i]]

        # 4. Handle Queries
        results = []
        for u, v in queries:
            if u == v:
                results.append(0)
            else:
                # Use binary lifting to find distance
                dist = 0
                curr_u, curr_v = rank[u], rank[v]
                if curr_u < curr_v:
                    # Move right
                    for k in range(LOG - 1, -1, -1):
                        if up[k][curr_u] < curr_v:
                            curr_u = up[k][curr_u]
                            dist += (1 << k)
                    results.append(dist + 1 if R[curr_u] >= curr_v else -1)
                else:
                    # Move left
                    for k in range(LOG - 1, -1, -1):
                        if down[k][curr_u] > curr_v:
                            curr_u = down[k][curr_u]
                            dist += (1 << k)
                    results.append(dist + 1 if L[curr_u] <= curr_v else -1)
        return results