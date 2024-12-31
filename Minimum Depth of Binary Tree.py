# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # If the root is None, the depth is 0.

        # If one of the subtrees is None, we consider only the other subtree's depth.
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        # If both subtrees exist, take the minimum of their depths.
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
