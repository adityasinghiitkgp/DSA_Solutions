def wordBreak(self, n, dict, s):
    ans=[]
    if s in dict:
        ans.append(s)
    for i in range(1,len(s)):
        word=s[i:]
        if word in dict:
            temp=s[0:i]
            p=self.wordBreak(n,dict,temp)
            for j in p:
                ans.append(j+" "+word)
    return ans