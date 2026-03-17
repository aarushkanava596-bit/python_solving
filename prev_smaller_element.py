class Solution:
    def prevSmaller(self, arr):
        stack = []
        res = []
        for num in arr:
            while stack and stack[-1] >= num:
                stack.pop()
            if stack:
                res.append(stack[-1])
            else:
                res.append(-1)
            stack.append(num)
        return res
