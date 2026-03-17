class Solution:
    def maxPeople(self, arr):
        n = len(arr)
        left = [0]*n
        right = [0]*n
        
        # Left pass using monotonic stack
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                left[i] += left[stack.pop()] + 1
            stack.append(i)
        
        # Right pass using monotonic stack
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                right[i] += right[stack.pop()] + 1
            stack.append(i)
        
        return max(left[i]+right[i]+1 for i in range(n))
