def removeConsecutiveCharacter(self, S):
    
    s=""
    for i in range(len(S)-1):
        if S[i]==S[i+1]:
            continue
        else:
            s+=S[i]
    if s and S[-1]!=s[-1]:
        s+=S[-1]
    if len(S)==1:
        s+=S[0]
    return s