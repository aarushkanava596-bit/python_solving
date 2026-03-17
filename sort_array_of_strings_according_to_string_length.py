class Solution:
    def sortByLength(self, arr):
        return str(arr.sort(key=len))
