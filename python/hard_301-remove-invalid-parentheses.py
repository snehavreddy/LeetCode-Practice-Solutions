class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        if not s:
            return [""]

        queue = [s]
        visited = {s}
        res = []
        found = False

        while queue:
            # Process all nodes at the current level
            level_size = len(queue)
            for _ in range(level_size):
                current = queue.pop(0)

                if is_valid(current):
                    res.append(current)
                    found = True

                # If a valid string is found at this level, we don't need to remove 
                # any more parentheses from this string to go deeper.
                if found:
                    continue

                # Generate all possible strings by removing one parenthesis
                for i in range(len(current)):
                    if current[i] not in ('(', ')'):
                        continue
                    
                    next_str = current[:i] + current[i+1:]
                    if next_str not in visited:
                        visited.add(next_str)
                        queue.append(next_str)
            
            # If we found valid strings at the current level (minimum removals), stop.
            if found:
                break

        return res