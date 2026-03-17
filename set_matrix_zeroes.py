class Solution:
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        row_zero = [False] * m
        col_zero = [False] * n
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_zero[i] = True
                    col_zero[j] = True
        
        for i in range(m):
            for j in range(n):
                if row_zero[i] or col_zero[j]:
                    matrix[i][j] = 0
