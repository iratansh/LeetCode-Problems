class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row == 0 and col == 0:
                    continue
                if row == 0 or col == 0:
                    if row == 0:
                        grid[row][col] += grid[row][col - 1]
                    if col == 0:
                        grid[row][col] += grid[row - 1][col]
                else:
                    grid[row][col] += min(grid[row][col - 1], grid[row - 1][col])

        return grid[-1][-1]
