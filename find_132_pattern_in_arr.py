class Solution:
    def has132Pattern(self, arr):
        stack = []
        s3 = float('-inf')
        for num in reversed(arr):
            if num < s3:
                return True
            while stack and stack[-1] < num:
                s3 = stack.pop()
            stack.append(num)
        return False
