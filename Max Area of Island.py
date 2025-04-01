class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(i, j):
            if (i < 0 or i == ROWS or j < 0 or j == COLS or grid[i][j] == 0 or (i, j) in visit):
                return 0

            visit.add((i, j))
            return ( 
                1 + 
                dfs(i + 1, j) +
                dfs(i - 1, j) +
                dfs(i, j + 1) +
                dfs(i, j - 1)
            )

        area = 0
        for i in range(ROWS):
            for j in range(COLS):
                area = max(area, dfs(i, j))
                    
        return area
