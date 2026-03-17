class Solution:
    def maxWater(self, arr):
        l, r = 0, len(arr) - 1
        left_max = right_max = water = 0
        
        while l < r:
            if arr[l] < arr[r]:
                if arr[l] >= left_max:
                    left_max = arr[l]
                else:
                    water += left_max - arr[l]
                l += 1
            else:
                if arr[r] >= right_max:
                    right_max = arr[r]
                else:
                    water += right_max - arr[r]
                r -= 1
                
        return water
