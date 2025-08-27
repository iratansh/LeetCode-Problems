# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        # return the node.val where node.val = avg(subtree(node.val))
        # dfs approach since we comput the average starting from that node to the leafs in all directions
        # run dfs on every node in root
        res = 0
        def dfs(node):
            if not node:
                return (0, 0)
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            total_sum = node.val + left_sum + right_sum
            total_count = left_count + right_count + 1
            if (total_sum // total_count) == node.val:
                nonlocal res
                res += 1
            
            return (total_sum, total_count)
        
        dfs(root)
        return res

