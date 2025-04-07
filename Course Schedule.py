class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # perform topological sorting on the prerequisites via Kahn's Algo
        # determine if a cycle exists and if it does return False else return True

        def topoSort(num_nodes, edges):
            # Step 1: Build adjacency list and in-degree array
            adj = defaultdict(list)
            in_degree = [0] * num_nodes

            for src, dest in edges:
                adj[src].append(dest)
                in_degree[dest] += 1

            # Step 2: Initialize queue with nodes of in-degree 0
            queue = deque([i for i in range(num_nodes) if in_degree[i] == 0])
            topo_order = []

            # Step 3: Process nodes
            while queue:
                node = queue.popleft()
                topo_order.append(node)

                for neighbor in adj[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

            # Step 4: Check for cycle (if not all nodes are in topo_order)
            if len(topo_order) != num_nodes:
                return False

            return True

        return topoSort(numCourses, prerequisites)
