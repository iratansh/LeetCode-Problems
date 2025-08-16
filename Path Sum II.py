# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # dfs question: perform dfs from root and explore all paths? And return all paths which sum to targetSum?
        # backtrack once you reach the leaf and then perform a dfs starting from that node
        paths = []

        def dfs(node, path, path_sum):
            if not node: 
                return
            path.append(node.val) # append the current node to the path
            path_sum += node.val
            
            # check if the curr_path_sum = targetSum
            if (not node.left and not node.right) and path_sum == targetSum:
                nonlocal paths
                paths.append(list(path))

            dfs(node.left, path, path_sum)
            dfs(node.right, path, path_sum)
            path.pop()
        
        dfs(root, [], 0)
        return paths
