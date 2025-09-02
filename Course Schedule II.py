class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # same as course schedule 1 just return the ordering this time
        # perform topo sort and return the top sorted array>?
        
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
                return [] # meaning that it isn't possible
            topo_order.reverse()
            return topo_order

        return topoSort(numCourses, prerequisites)
