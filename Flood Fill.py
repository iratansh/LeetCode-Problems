class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        dRow = [ -1, 0, 1, 0]
        dCol = [ 0, 1, 0, -1]
        rows, cols = len(image), len(image[0])

        def isValid(vis, row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return False
            if vis[row][col]:
                return False
            if image[row][col] != original_color:
                return False
            return True
        
        def bfs(grid, vis, row, col):
            queue = deque()
            queue.append((row, col))
            vis[row][col] = True

            while queue:
                cell = queue.popleft()
                x = cell[0]
                y = cell[1]
                image[x][y] = color
                for i in range(4):
                    adjx = x + dRow[i]
                    adjy = y + dCol[i]
                    if (isValid(vis, adjx, adjy)):
                        queue.append((adjx, adjy))
                        vis[adjx][adjy] = True

        vis = [[False for _ in range(cols)] for _ in range(rows)]
        bfs(image, vis, sr, sc)
        image[sr][sc] =color
        return image
