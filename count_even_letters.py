from collections import Counter

class Solution:
    def count(self, s):
        freq = Counter(s)
        return sum(1 for val in freq.values() if val % 2 == 0)
