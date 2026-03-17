class Solution:
    def median(self, mat):
        n = len(mat)
        m = len(mat[0])
        arr = []
        for row in mat:
            arr.extend(row)
        arr.sort()
        total = n * m
        return arr[total // 2]
