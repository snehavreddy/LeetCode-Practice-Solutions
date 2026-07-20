class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        total_elements = m * n
        
        # Optimize k if it's larger than the number of elements
        k = k % total_elements
        
        # Flatten the grid into a 1D list
        flat_list = []
        for row in grid:
            for val in row:
                flat_list.append(val)
        
        # Perform the shift by rearranging the flat list
        # The new list starts from the element at index (total - k)
        shifted_list = flat_list[-k:] + flat_list[:-k]
        
        # Reconstruct the 2D grid from the shifted 1D list
        new_grid = []
        for i in range(m):
            new_grid.append(shifted_list[i * n : (i + 1) * n])
            
        return new_grid