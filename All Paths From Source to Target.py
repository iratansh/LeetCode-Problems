class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []
        queue = deque()
        
        queue.append([0])
        
        while queue:
            path = queue.popleft()
            last_node = path[-1]
            
            # If the path ends at the target node, add it to the result
            if last_node == n - 1:
                res.append(path)
            else:
                # Otherwise, extend the path by all neighbors of the last node
                for neighbor in graph[last_node]:
                    new_path = path + [neighbor]
                    queue.append(new_path)
        
        return res
