class Solution:
    def equalPartition(self, arr):
        n = len(arr)
        total = sum(arr)
        target = total // 2
        
        sizes = {n // 2} if n % 2 == 0 else {n // 2, n // 2 + 1}
        
        for mask in range(1 << n):
            subset = []
            s = 0
            
            for i in range(n):
                if mask & (1 << i):
                    subset.append(arr[i])
                    s += arr[i]
            
            if s == target and len(subset) in sizes:
                other = arr[:]
                for x in subset:
                    other.remove(x)
                return [subset, other]
