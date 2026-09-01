from typing import List
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter_idx = {}
        sx = sy = -1
        
        # Step 1: Find the start position and assign a unique bit index to each litter
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    sx, sy = i, j
                elif classroom[i][j] == 'L':
                    litter_idx[(i, j)] = len(litter_idx)
                    
        num_litter = len(litter_idx)
        full_mask = (1 << num_litter) - 1
        
        # If there is no litter to clean, 0 moves are required
        if num_litter == 0:
            return 0
            
        # Step 2: 3D array to store the maximum energy we've had at a specific (x, y, mask) state
        # This acts as our visited set but allows us to revisit if we arrive with strictly MORE energy
        best_energy = [[[-1] * (1 << num_litter) for _ in range(n)] for _ in range(m)]
        
        # Queue stores: (row, col, collected_litter_mask, current_energy, steps)
        q = deque([(sx, sy, 0, energy, 0)])
        best_energy[sx][sy][0] = energy
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Step 3: BFS Traversal
        while q:
            r, c, mask, e, steps = q.popleft()
            
            # If we've collected all the litter, return the current steps
            if mask == full_mask:
                return steps
                
            # We can only move to adjacent cells if we have energy greater than 0
            if e == 0:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check bounds and make sure it's not an obstacle
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    nxt_e = e - 1
                    
                    # Reset energy to maximum capacity if stepping on 'R'
                    if classroom[nr][nc] == 'R':
                        nxt_e = energy
                        
                    nxt_mask = mask
                    # Update mask if we collected a new piece of litter
                    if (nr, nc) in litter_idx:
                        nxt_mask |= (1 << litter_idx[(nr, nc)])
                        
                    # State Pruning: Only queue this path if it arrives at (nr, nc) with a specific
                    # mask and has MORE energy than any previous path that reached this exact state.
                    if nxt_e > best_energy[nr][nc][nxt_mask]:
                        best_energy[nr][nc][nxt_mask] = nxt_e
                        q.append((nr, nc, nxt_mask, nxt_e, steps + 1))
                        
        return -1