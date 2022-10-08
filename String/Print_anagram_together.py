from collections import defaultdict
class Solution:
    def Anagrams(self, words, n):

        d=defaultdict(list)
        for i in words:
            s="".join(sorted(i))
            d[s].append(i)
        lis=[]
        for val in d.values():
            lis.append(val)
        return lis