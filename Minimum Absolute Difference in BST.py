# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inOrderTrav(node):
            if node:
                inOrderTrav(node.left)
                if self.prevVal is not None: 
                    self.minDistance = min(self.minDistance, node.val - self.prevVal)
                self.prevVal = node.val
                inOrderTrav(node.right)
        
        self.minDistance = float("inf")
        self.prevVal = None  
        inOrderTrav(root)
        return self.minDistance
