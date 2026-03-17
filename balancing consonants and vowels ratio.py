class Solution:
    def countBalanced(self, arr):
        vowels = set('aeiou')
        prefix = [0]
        for s in arr:
            v = sum(1 for c in s if c in vowels)
            c = len(s) - v
            prefix.append(prefix[-1] + (v - c))
        
        from collections import Counter
        freq = Counter(prefix)
        count = 0
        for val in freq.values():
            count += val * (val - 1) // 2  # nC2 pairs
        return count
