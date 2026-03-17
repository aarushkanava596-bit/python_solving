class Solution:
    def scoreOfParentheses(self, s):
        stack = [0]
        for char in s:
            if char == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += 1 if v == 0 else 2 * v
        return stack[0]
