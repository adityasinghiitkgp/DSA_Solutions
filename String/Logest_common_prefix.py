
def longestCommonPrefix(self,strs):
    mini=10*99
    s=0
    for i in strs:
        if mini>len(i):
            mini=len(i)
            s=i
    ans=""
    for i in range(mini):
        for j in strs:
            if j[i]!=s[i]:
                return ans
        ans+=str(s[i])
    return ans
            
            
                    