class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def check(grid, i, j, m, n):
            p=0
            if(i==0 or grid[i-1][j]==0):
                p+=1
            if(i==m or grid[i+1][j]==0):
                p+=1
            if(j==0 or grid[i][j-1]==0):
                p+=1
            if(j==n or grid[i][j+1]==0):
                p+=1
            return p

        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += check(grid, i, j, len(grid) - 1, len(grid[0]) - 1)
        return perimeter
