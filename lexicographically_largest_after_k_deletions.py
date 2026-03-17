class Solution:
    def maxSubseq(self, s, k):
        #code here
        a=[]
        for i in s:
            while len(a) and a[-1]<i and k:
                a.pop()
                k-=1
            a.append(i)
        while k:
            a.pop()
            k-=1
        return "".join(a)

