# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # traverse though BST to find nodes such that node.val >= low or node.val <= high
        # have a cum_sum and add to it while traversing the tree
        cum_sum = 0
        def traverse(node):
            if not node:
                return
            nonlocal cum_sum
            if node.val >= low and node.val <= high:
                cum_sum += node.val
            traverse(node.left)
            traverse(node.right)

            return cum_sum
        
        return traverse(root)
