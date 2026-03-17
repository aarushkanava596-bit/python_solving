class Solution:
    def getMinDiff(self, arr, k):
        arr.sort()
        n = len(arr)
        ans = arr[n-1] - arr[0]
        small = arr[0] + k
        big = arr[n-1] - k
        if small > big:
            small, big = big, small
        for i in range(n-1):
            if arr[i+1] - k < 0:
                continue
            mn = min(small, arr[i+1] - k)
            mx = max(big, arr[i] + k)
            ans = min(ans, mx - mn)
        return ans
