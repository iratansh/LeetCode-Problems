class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        dic = {'row':[], 'col':[]}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    dic['row'].append(i)
                    dic['col'].append(j)
        
        for i in dic['row']:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
            
        for i in dic['col']:
            for j in range(len(matrix)):
                matrix[j][i] = 0
