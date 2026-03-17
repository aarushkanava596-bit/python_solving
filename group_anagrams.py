class Solution:
    def groupAnagrams(self, strs):
        from collections import defaultdict
        d = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            d[key].append(s)
        return list(d.values())
