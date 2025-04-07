class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # input = adj matrix 
        # find total number of provinces through bfs
        n = len(isConnected)  
        visited = [False] * n

        def bfs(start):
            queue = deque([start])
            visited[start] = True

            while queue:
                node = queue.popleft()
                for neighbor in range(n):
                    if isConnected[node][neighbor] == 1 and not visited[neighbor]:
                        queue.append(neighbor)
                        visited[neighbor] = True
    
        num_provinces = 0
        for i in range(n):
            if not visited[i]:
                bfs(i)
                num_provinces += 1
        return num_provinces
