class Solution:
    def minMen(self, arr):
        n = len(arr)
        intervals = []
        for i, r in enumerate(arr):
            if r != -1:
                start = max(0, i - r)
                end = min(n - 1, i + r)
                intervals.append((start, end))
        intervals.sort()
        res = 0
        idx = 0
        i = 0
        while i < len(intervals):
            farthest = -1
            while i < len(intervals) and intervals[i][0] <= idx:
                farthest = max(farthest, intervals[i][1])
                i += 1
            if farthest < idx:
                return -1
            res += 1
            idx = farthest + 1
            if idx >= n:
                return res
        return -1
