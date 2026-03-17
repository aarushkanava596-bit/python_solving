class Solution:
    def minSwaps(self, s1, s2):
        if len(s1) != len(s2):
            return -1
        
        count10 = count01 = 0
        for a, b in zip(s1, s2):
            if a == '1' and b == '0':
                count10 += 1
            elif a == '0' and b == '1':
                count01 += 1
        
        if (count10 + count01) % 2 != 0:
            return -1
        
        return count10 // 2 + count01 // 2 + (count10 % 2) * 2
