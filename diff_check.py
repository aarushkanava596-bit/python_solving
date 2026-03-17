class Solution:
    def minDifference(self, arr):
        times = []
        for t in arr:
            h, m, s = map(int, t.split(':'))
            times.append(h * 3600 + m * 60 + s)
        
        times.sort()
        min_diff = float('inf')
        n = len(times)
        
        for i in range(1, n):
            min_diff = min(min_diff, times[i] - times[i-1])
        
        min_diff = min(min_diff, 86400 - (times[-1] - times[0]))
        return min_diff
