# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return
            if node.val == 0 or node.val == 1:
                return bool(node.val)
            
            right = dfs(node.right)
            left = dfs(node.left)
            if node.val == 2:
                return right or left
            if node.val == 3:
                return right and left
            return False
        return dfs(root)
