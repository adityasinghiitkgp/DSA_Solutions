def reverseString(self, s):
    i=0
    l=len(s)-1
    while i<l:
        s[i],s[l]=s[l],s[i]
        i+=1
        l-=1
    return s