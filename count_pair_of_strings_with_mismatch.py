class Solution:
    def countPairs(self, arr):
        from collections import defaultdict
        
        count = 0
        n = len(arr[0])
        masks = defaultdict(int)
        
        for word in arr:
            for i in range(n):
                masked = word[:i] + '*' + word[i+1:]
                count += masks[masked]
                masks[masked] += 1
        
        return count
