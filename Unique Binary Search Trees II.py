# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate(left, right): # recursive function
            if left == right: # base case: check if left == right
                return [TreeNode(left)]
            if left > right: # base case: check if left > right
                return [None]
        
            res = []
            for val in range(left, right + 1): # iterate starting from left to right
                for leftTree in generate(left, val - 1):  # iterate through the list of nodes returned by generate function
                    for rightTree in generate(val + 1, right): # iterate through list of nodes returned by generate function
                        root = TreeNode(val, leftTree, rightTree) 
                        res.append(root)
            return res
        return generate(1, n)
