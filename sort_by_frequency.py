class Solution:
    def frequencySort(self, s):
        from collections import Counter
        freq = Counter(s)
        return ''.join(sorted(s, key=lambda x: (freq[x], x)))
