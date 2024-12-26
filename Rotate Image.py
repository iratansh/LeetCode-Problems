class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        NROWS = len(matrix)
        top = 0
        bottom = NROWS - 1

        # Reverse the matrix 
        while top < bottom:
            for col in range(NROWS):
                temp = matrix[top][col]
                matrix[top][col] = matrix[bottom][col]
                matrix[bottom][col] = temp
            top += 1
            bottom -= 1

        # Transpose the matrix 
        for row in range(NROWS):
            for col in range(row + 1, NROWS):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp
