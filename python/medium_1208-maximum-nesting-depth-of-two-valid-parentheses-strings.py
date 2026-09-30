class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        depth = 0
        
        for char in seq:
            if char == '(':
                # Assign to 0 or 1 based on current depth parity before going deeper
                ans.append(depth % 2)
                depth += 1
            else:
                # Decrease depth first to match the depth of the corresponding '('
                depth -= 1
                ans.append(depth % 2)
                
        return ans