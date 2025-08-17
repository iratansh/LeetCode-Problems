# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        # validate that the current subtree is a BST first 
        # then find sum of the entire subtree?
        # compare with other possible subtrees in the binary tree and return the max one
        maxSum = 0
        def postOrder(node):
            if not node:
                # An empty tree is a valid BST with sum=0
                return True, 0, float('inf'), float('-inf')
            
            left_is_bst, left_sum, left_min, left_max = postOrder(node.left)
            right_is_bst, right_sum, right_min, right_max = postOrder(node.right)

            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                nonlocal maxSum
                curr_sum = left_sum + right_sum + node.val
                maxSum = max(maxSum, curr_sum)  # update global
                return True, curr_sum, min(node.val, left_min), max(node.val, right_max)
            else:
                return False, 0, 0, 0

        postOrder(root)
        return maxSum
