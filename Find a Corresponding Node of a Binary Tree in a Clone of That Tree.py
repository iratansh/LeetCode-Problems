# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # traverse through both trees simulatenously -> find the corresponding node in target such that it lies in the position where original node = target
        def dfs(node1, node2):
            if not node1 or not node2:
                return 
            if node1 == target:
                return node2
            
            left = dfs(node1.left, node2.left)
            if left:
                return left
            right = dfs(node1.right, node2.right)
            if right:
                return right


        return dfs(original, cloned) 
