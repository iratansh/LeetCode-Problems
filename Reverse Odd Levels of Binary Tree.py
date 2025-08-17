# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # bfs problem: basically just reverse every odd level, keep in mind though that the root is the 0th level
        # so would this just a be a basic bfs but after the level is completed we updated the node's value to be the correct value?
        def bfs():
            queue = deque()
            queue.append(root)
            curr_level = 0
            while queue:
                queue_len = len(queue)
                level = []
                level_vals = []
                for i in range(queue_len):
                    node = queue.popleft()
                    if node:
                        queue.append(node.left)
                        level.append(node)
                        level_vals.append(node.val)
                        queue.append(node.right)
                if level and curr_level % 2 == 1:
                    # now perform the node.val update for each node in level
                    level_vals.reverse()
                    for i in range(0, len(level)):
                        level[i].val = level_vals[i]
                curr_level += 1

        bfs()
        return root
