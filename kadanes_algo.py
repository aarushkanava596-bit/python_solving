class Solution:
    def maxSubarraySum(self, arr):
        max_sum = curr = arr[0]
        for x in arr[1:]:
            curr = max(x, curr + x)
            max_sum = max(max_sum, curr)
        return max_sum
