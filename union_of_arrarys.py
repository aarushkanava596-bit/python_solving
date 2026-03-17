class Solution:    
    def findUnion(self, a, b):
        s = set(a)
        for num in b:
            s.add(num)
        return list(s)
