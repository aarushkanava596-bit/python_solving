class Solution:
    def combinationSum(self, n, k):
        res = []
        def backtrack(start, path, target):
            if len(path) == k:
                if target == 0:
                    res.append(path[:])
                return
            for i in range(start, 10):
                if i > target:
                    break
                path.append(i)
                backtrack(i+1, path, target - i)
                path.pop()
        backtrack(1, [], n)
        return res
