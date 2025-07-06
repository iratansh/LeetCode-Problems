# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sortedArr = []

        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            sortedArr.append(node.val)
            inOrder(node.right)

        def constructBST(arr):
            if len(arr) == 0:
                return None
            mid = len(arr) // 2
            root = TreeNode(arr[mid])
            root.left = constructBST(arr[:mid])
            root.right = constructBST(arr[mid + 1:])
            return root
            
        inOrder(root)
        return constructBST(sortedArr)
