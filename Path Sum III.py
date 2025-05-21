# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        def dfs(node, psum):
            if not node:
                return 0
            psum += node.val
            res = 1 if psum == targetSum else 0
            res += dfs(node.left, psum)
            res += dfs(node.right, psum)
            return res
        
        return (dfs(root, 0) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum))
            
