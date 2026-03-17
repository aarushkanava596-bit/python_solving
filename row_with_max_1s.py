class Solution:
    def rowWithMax1s(self, arr):
        n, m = len(arr), len(arr[0])
        i, j = 0, m - 1
        ans = -1
        
        while i < n and j >= 0:
            if arr[i][j] == 1:
                ans = i
                j -= 1
            else:
                i += 1
                
        return ans
