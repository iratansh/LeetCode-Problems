# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        total = 0

        def calculateTilt(node):
            nonlocal total
            if not node:
                return 0
            left = calculateTilt(node.left)
            right = calculateTilt(node.right)            
            tilt = abs(left - right)

            total += tilt
            return left + right + node.val
        calculateTilt(root)
        return total
