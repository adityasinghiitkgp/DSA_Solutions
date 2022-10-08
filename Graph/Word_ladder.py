from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        d=defaultdict(list)
        for i in wordList:
            for j in range(len(i)):
                x=i[0:j]+"-"+i[j+1:]
                d[x].append(i)
        
        lis=[]
        lis.append([1,beginWord])
        s=set()

        while lis:
            dist,word=lis.pop(0)
            if word==endWord:
                return dist
            if word not in s:
                s.add(word)
                for i in range(len(word)):
                    x=word[0:i]+"-"+word[i+1:]
                    if x in d:
                        for j in d[x]:
                            lis.append([dist+1,j])
        return 0