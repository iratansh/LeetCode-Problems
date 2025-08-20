class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Find the connected components using BFS
        # Count number of nodes + edges in each component 
        # complete component = n(n-1)/2 = E
        # given an array of edges: do i convert it to an adj list or can i use it on its own?
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def bfs(start, adj, visited):
            component = []
            q = deque([start])
            visited[start] = True
            
            while q:
                node = q.popleft()
                component.append(node)
                for nei in adj[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        q.append(nei)
            
            return component

        
        visited = [False] * n
        res = 0
        for i in range(n):
            if not visited[i]:
                comp = bfs(i, adj, visited)
                component_set = set(comp)
                count_edges = 0
                for u in comp:
                    for v in adj[u]:
                        if v in component_set:
                            count_edges += 1
                count_edges //= 2  # each edge counted twice

                num_vertices = len(comp)
                if count_edges == num_vertices * (num_vertices - 1) // 2:
                    res += 1

        return res    
