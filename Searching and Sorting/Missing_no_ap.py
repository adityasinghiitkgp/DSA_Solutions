def inSequence(self, A, B, C):
    if (A-B)==0:
        return 1
        
    
    if (A-B)>0:
        if C<0 and (A-B)%C==0:
            return 1
        else:
            return 0
    else:
        if C>0 and (A-B)%C==0:
            return 1
        else:
            return 0