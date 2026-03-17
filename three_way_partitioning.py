class Solution:
    def threeWayPartition(self, arr, a, b):
        n = len(arr)
        low, mid, high = 0, 0, n - 1
        while mid <= high:
            if arr[mid] < a:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif a <= arr[mid] <= b:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
        return True
