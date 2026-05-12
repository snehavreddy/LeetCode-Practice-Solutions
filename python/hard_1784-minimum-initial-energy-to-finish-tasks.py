class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # Sort tasks by the difference (minimum - actual) descending
        # This prioritizes tasks that require a larger 'cushion' to start
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        
        res = 0
        current_energy = 0
        
        for actual, minimum in tasks:
            # If current energy is less than the minimum required for this task
            if current_energy < minimum:
                # Add the deficit to our total initial energy requirement
                res += (minimum - current_energy)
                # Update current energy to the minimum required to start
                current_energy = minimum
            
            # Spend the actual energy required for the task
            current_energy -= actual
            
        return res