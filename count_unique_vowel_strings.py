from math import factorial
from collections import Counter

class Solution:
    def vowelCount(self, s):
        freq = Counter(c for c in s if c in "aeiou")
        if not freq:
            return 0
        product = 1
        for v in freq:
            product *= freq[v]
        return product * factorial(len(freq))
