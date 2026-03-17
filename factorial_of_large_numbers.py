class Solution:
    def factorial(self, n):
        f = 1
        for i in range(2, n + 1):
            f *= i
        return [int(d) for d in str(f)]
