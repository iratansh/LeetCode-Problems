class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prevHeight):
            if (
                r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                (r, c) in visited or 
                heights[r][c] < prevHeight
            ):
                return

            visited.add((r, c))
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                new_r, new_c = dr + r, dc + c
                dfs(new_r, new_c, visited, heights[r][c])
        
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])      
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c]) 
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])       
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])
        
        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])
        return result
