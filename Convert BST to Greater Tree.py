# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # each node's new value = node.val + i.val such that i.val > node.val
        cum_sum = 0
        def reverse_inOrder(node):
            if not node:
                return 
            nonlocal cum_sum
            reverse_inOrder(node.right)
            cum_sum += node.val
            node.val = cum_sum
            reverse_inOrder(node.left)
            return cum_sum
            
        reverse_inOrder(root)
        return root
