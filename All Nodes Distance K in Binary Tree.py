# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        from collections import deque
        adjList = {}
        res = []

        def buildGraph(node, parent, adjList):
            if not node:
                return
            
            if node.val not in adjList:
                adjList[node.val] = []
            
            if parent:
                adjList[node.val].append(parent.val)
                adjList[parent.val].append(node.val)
            
            buildGraph(node.left, node, adjList)
            buildGraph(node.right, node, adjList)

        def graphBFS(adjList, k, target):
            q = deque([(target.val, 0)])
            visited = set()
            visited.add(target.val)

            while q:
                node, dist = q.popleft()
                if dist == k:
                    res.append(node)
                if dist > k:
                    break
                
                for neighbor in adjList[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append((neighbor, dist + 1))
        
        buildGraph(root, None, adjList)
        graphBFS(adjList, k, target)
        return res
