def getMaxArea(self,histogram):
    stack=[]
    maxi=0
    index=0
    
    while index<len(histogram):
        if not stack or histogram[stack[-1]]<=histogram[index]:
            stack.append(index)
            index+=1
        
        else:
            pre_index=stack.pop()
            if not stack:
                maxi=max(maxi,histogram[pre_index]*index)
            else:
                maxi=max(maxi,histogram[pre_index]*(index-stack[-1]-1))
    
    while stack:
        pre_index=stack.pop()
        if not stack:
            maxi=max(maxi,histogram[pre_index]*index)
        else:
            maxi=max(maxi,histogram[pre_index]*(index-stack[-1]-1))
    return maxi