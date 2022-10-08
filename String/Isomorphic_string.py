def areIsomorphic(self,str1,str2):
    d={}
    if len(str1)!=len(str2):
        return False
    for i in range(len(str1)):
        if str1[i] not in d:
            d[str1[i]]=str2[i]
        else:
            if d[str1[i]]!=str2[i]:
                return False
    d={}
    for i in range(len(str2)):
        if str2[i] not in d:
            d[str2[i]]=str1[i]
        else:
            if d[str2[i]]!=str1[i]:
                return False
    return True