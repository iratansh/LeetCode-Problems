class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        R = [[0] * len(row) for row in triangle]
        R[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(i + 1):
                if j == 0:
                    R[i][j] = R[i - 1][j] + triangle[i][j] # only consider top element
                elif j == i:
                    R[i][j] = R[i - 1][j - 1] + triangle[i][j] # only consider left top element
                else:
                    R[i][j] = min(R[i - 1][j], R[i - 1][j - 1]) + triangle[i][j] # consider both
        
        return min(R[-1])
