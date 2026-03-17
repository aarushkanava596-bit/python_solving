from collections import Counter

class Solution:
    def substrWithVowels(self, s1, s2):
        required = set(s1)
        n = len(s2)
        left = 0
        min_len = float('inf')
        window_count = Counter()
        formed = 0

        for right, char in enumerate(s2):
            if char in required:
                window_count[char] += 1
                if window_count[char] == 1:
                    formed += 1

            while formed == len(required) and left <= right:
                min_len = min(min_len, right - left + 1)
                if s2[left] in required:
                    window_count[s2[left]] -= 1
                    if window_count[s2[left]] == 0:
                        formed -= 1
                left += 1

        return min_len if min_len != float('inf') else -1
