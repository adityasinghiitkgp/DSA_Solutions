def subArrayExists(self,arr,n):
    s=set()
    sumi=0
    for i in arr:
        if i==0:
            return True
        sumi+=i
        if sumi in s or sumi==0:
            return True
        else:
            s.add(sumi)
        
    return False