class Solution:
    def winner(self, arr):
        from collections import Counter
        freq = Counter(arr)
        max_votes = max(freq.values())
        winners = [name for name, count in freq.items() if count == max_votes]
        return [min(winners), str(max_votes)]
