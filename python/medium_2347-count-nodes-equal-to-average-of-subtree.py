# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.result_count = 0
        
        def post_order(node):
            if not node:
                # Return (sum_of_nodes, count_of_nodes)
                return 0, 0
            
            # Recursively get sum and count for left and right subtrees
            left_sum, left_count = post_order(node.left)
            right_sum, right_count = post_order(node.right)
            
            # Calculate sum and count for the current subtree
            current_sum = left_sum + right_sum + node.val
            current_count = left_count + right_count + 1
            
            # Check if the average matches the current node's value (integer division for rounding down)
            if current_sum // current_count == node.val:
                self.result_count += 1
                
            return current_sum, current_count
        
        post_order(root)
        return self.result_count