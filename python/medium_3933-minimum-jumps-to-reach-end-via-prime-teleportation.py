from collections import deque, defaultdict

# Pre-compute SPF (Smallest Prime Factor) once for all test cases
MAX = 10**6 + 1
spf = list(range(MAX))
for i in range(2, int(MAX**0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, MAX, i):
            if spf[j] == j:
                spf[j] = i

class Solution:
    def minJumps(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
            
        # 1. Map each prime factor to the indices where it appears
        # This allows O(1) lookups for teleportation destinations
        prime_to_indices = defaultdict(list)
        for idx, val in enumerate(nums):
            temp = val
            while temp > 1:
                p = spf[temp]
                prime_to_indices[p].append(idx)
                while temp % p == 0:
                    temp //= p
        
        # 2. BFS for shortest path
        queue = deque([0])
        visited_idx = {0}
        # Track which primes have already been used for teleportation to avoid cycles/redundancy
        visited_primes = set()
        steps = 0
        
        while queue:
            for _ in range(len(queue)):
                curr_idx = queue.popleft()
                
                if curr_idx == n - 1:
                    return steps
                
                # Option A: Adjacent moves (+1, -1)
                for neighbor in (curr_idx - 1, curr_idx + 1):
                    if 0 <= neighbor < n and neighbor not in visited_idx:
                        visited_idx.add(neighbor)
                        queue.append(neighbor)
                
                # Option B: Prime Teleportation
                # We can teleport if nums[curr_idx] is a prime
                val = nums[curr_idx]
                if val > 1 and spf[val] == val:
                    # If this prime hasn't been used to teleport yet
                    if val in prime_to_indices:
                        for neighbor in prime_to_indices[val]:
                            if neighbor not in visited_idx:
                                visited_idx.add(neighbor)
                                queue.append(neighbor)
                        # CRITICAL: Remove prime from map after use to keep it O(V + E)
                        del prime_to_indices[val]
                        
            steps += 1
            
        return -1