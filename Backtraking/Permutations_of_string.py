def find_permutation(self, S):
    if len(S)==1:
        return S
    ans=[]
    for i in range(len(S)):
        new=self.find_permutation(S[0:i]+S[i+1:])
        for j in new:
            ans.append(S[i]+j)
    ans.sort()
    return ans