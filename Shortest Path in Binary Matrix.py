class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # 0 represents no obstacle, 1 represents an obstacle
        # bfs question starting from grid[0][0] - navigate to the bottom right cell
        # most efficient path can be defined as the path that allows the player to go to the goal using the least amount of jumps
        n = len(grid)
        vis = [[ False for i in range(len(grid[0]))] for i in range(n)]
        dRow = [-1,-1,-1,0,0,1,1,1]
        dCol = [-1,0,1,-1,1,-1,0,1]

        def isValid(vis, row, col):
            if (row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0])):
                return False
            if vis[row][col]:
                return False
            if grid[row][col] == 1:
                return False
            return True
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        def bfs(vis, row, col):
            q = deque()
            q.append((row, col, 1))
            vis[row][col] = True

            while (len(q) > 0):
                cell = q.popleft()
                x = cell[0]
                y = cell[1]

                if x == n-1 and y == n-1:
                    return cell[2]


                for i in range(8):
                    adjx = x + dRow[i]
                    adjy = y + dCol[i]
                    if (isValid(vis, adjx, adjy)):
                        q.append((adjx, adjy, cell[2] + 1))
                        vis[adjx][adjy] = True
            return -1
        return bfs(vis, 0, 0)
