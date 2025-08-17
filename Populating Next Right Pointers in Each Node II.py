"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # perform a bfs and then set the next pointers across each row
        queue = deque()
        queue.append(root)
        
        def bfs():
            while queue:
                queue_len = len(queue)
                level = []
                for i in range(queue_len):
                    node = queue.popleft()
                    if node:
                        level.append(node)
                        queue.append(node.left)
                        queue.append(node.right)
                if level: # now we set the next pointers across each row
                    i = 0
                    curr = level[i]
                
                    for i in range(len(level) - 1):
                        level[i].next = level[i + 1]
                    level[-1].next = None

        bfs()
        return root
