class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # use topo sort to build a 2D matrix representation of a graph following the requirements listed in the condition input arrays
        #  really only the ints from 1-k need to be considered - any spaces can be set to 0
        # how do you turn this into a graph though? Each array of conditions can be thought of as a directed graph
        # so we are given 2 DAG's
        # Apply Topo sort on each DAG -> orderubg of all numbers
        def topologicalSort(V, edges):
            adj = defaultdict(list)
            indegree = [0] * V
        
            for a, b in edges:
                adj[a-1].append(b-1)

            # Calculate indegree of each vertex
            for u in range(V):
                for v in adj[u]:
                    indegree[v] += 1
            

            # Queue to store vertices with indegree 0
            q = deque([i for i in range(V) if indegree[i] == 0])
            
            result = []
            while q:
                node = q.popleft()
                result.append(node)

                for neighbor in adj[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        q.append(neighbor)

            # Check for cycle
            if len(result) != V:
                return []

            return result
        
        sorted_row = topologicalSort(k, rowConditions)
        sorted_col = topologicalSort(k, colConditions)
        if not sorted_row or not sorted_col:
            return []
        row_pos = {num: i for i, num in enumerate(sorted_row)}
        col_pos = {num: j for j, num in enumerate(sorted_col)}

        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k+1):
            i, j = row_pos[num-1], col_pos[num-1]
            matrix[i][j] = num

        return matrix
