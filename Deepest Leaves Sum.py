# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # just reutrn the sum of the leaf nodes
        # classic bfs

        def bfs():
            res = []
            q = deque([root])

            while q:
                level = []

                for i in range(len(q)):
                    node = q.popleft()
                    if node:
                        q.append(node.left)
                        q.append(node.right)
                        level.append(node.val)
                if level:
                    res.append(level)
            return sum(res[-1])

        
        return bfs()
