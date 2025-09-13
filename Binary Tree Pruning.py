# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # remove subtrees such that they don't contain a 1
        # looks like a dfs question
        
        def dfs(node):
            if not node: # reached the end of the subtree
                return False
            
            left = dfs(node.left)
            if not left:
                node.left = None
            right = dfs(node.right)
            if not right:
                node.right = None
            return (node.val == 1) or left or right
            
        return root if dfs(root) else None       
            
