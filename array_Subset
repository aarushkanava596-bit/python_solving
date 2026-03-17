class Solution:
    def isSubset(self, a, b):
        from collections import Counter
        ca = Counter(a)
        cb = Counter(b)
        for k in cb:
            if ca[k] < cb[k]:
                return False
        return True
