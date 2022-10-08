def ispar(self,x):
    lis=[]
    for i in x:
        if i in ("[","(","{"):
            lis.append(i)
        
        
        else:
            
            if len(lis)==0:
                return False
            v=lis.pop()
            
            if v=="{" and i!="}":
                return False
            elif v=="[" and i!="]":
                return False
            elif v=="(" and i!=")":
                return False
    if lis:
        return False
    return True
