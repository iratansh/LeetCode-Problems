# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # dfs question return the parent of the deepest subtree
        # this can be found by running dfs on the root and recording the depth of the path
        
        def dfs(node, depth):
            if not node:
                return (None, depth - 1)
            
            leftN, leftD = dfs(node.left, depth + 1)
            rightN, rightD = dfs(node.right, depth + 1)
            if leftD == rightD:
                return (node, leftD)

            return (leftN, leftD) if leftD > rightD else (rightN, rightD)

        
        maxN, maxD = dfs(root, 0)
        return maxN
