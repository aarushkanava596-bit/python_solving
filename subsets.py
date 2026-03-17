class Solution:
    def subsets(self, nums):
        res = []
        n = len(nums)
        def backtrack(start, path):
            res.append(path[:])
            for i in range(start, n):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        backtrack(0, [])
        return res
