class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack = []
        groups = []
        current = {""}
        
        for char in expression:
            if char == '{':
                # Push the current state to the stack and start a new level
                stack.append((groups, current))
                groups = []
                current = {""}
                
            elif char == '}':
                # Union all the sets in the current level
                level_set = set().union(*groups, current)
                
                # Pop the previous state from the stack
                prev_groups, prev_current = stack.pop()
                
                # Concatenate the previous current set with the evaluated level set
                current = {a + b for a in prev_current for b in level_set}
                groups = prev_groups
                
            elif char == ',':
                # Finished one part of a union, add it to groups and reset current
                groups.append(current)
                current = {""}
                
            else:
                # Concatenate the character to all prefixes in the current set
                current = {a + char for a in current}
                
        # Final union of any remaining groups and the current set
        final_set = set().union(*groups, current)
        
        # Return the sorted list of unique words
        return sorted(list(final_set))