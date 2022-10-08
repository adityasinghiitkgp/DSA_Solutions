def convert(n):
    if n=="I":
        return 1
    elif n=="V":
        return 5
    elif n=="X":
        return 10
    elif n=="L":
        return 50
    elif n=="C":
        return 100
    elif n=="D":
        return 500
    else:
        return 1000
class Solution:
    def romanToDecimal(self, S):
        s=0
        i=0
        while i<(len(S)):
            if i+1<len(S):
                x=convert(S[i])
                y=convert(S[i+1])
                if x<y:
                    s+=(y-x)
                    i+=2
                else:
                    s+=x
                    i+=1
            else:
                s+=convert(S[i])
                i+=1
        return s
            