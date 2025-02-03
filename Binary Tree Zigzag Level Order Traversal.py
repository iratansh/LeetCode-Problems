# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = collections.deque([root])
        level_num = 0

        while queue:
            queue_len = len(queue)
            level = []
            for i in range(queue_len):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level_num % 2:
                level.reverse()
            
            res.append(level)
            level_num += 1
        return res
