# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])

        # Partition rest of array into left (< root) and right (> root)
        left_vals = [x for x in preorder[1:] if x < preorder[0]]
        right_vals = [x for x in preorder[1:] if x > preorder[0]]

        root.left = self.bstFromPreorder(left_vals)
        root.right = self.bstFromPreorder(right_vals)
        return root
