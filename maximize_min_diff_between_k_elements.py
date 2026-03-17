class Solution:
    def maxMinDiff(self, arr, k):
        arr.sort()
        
        def can(d):
            count = 1
            prev = arr[0]
            
            for i in range(1, len(arr)):
                if arr[i] - prev >= d:
                    count += 1
                    prev = arr[i]
                if count >= k:
                    return True
            return False
        
        low, high = 0, arr[-1] - arr[0]
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            if can(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
