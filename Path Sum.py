# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, sum):
            if not node:
                return False
            if node.val == sum and not node.right and not node.left:
                return True
            if node.left:
                node.left.val += node.val
            if node.right:
                node.right.val += node.val

            return dfs(node.left, sum) or dfs(node.right, sum)
        return dfs(root, targetSum)
