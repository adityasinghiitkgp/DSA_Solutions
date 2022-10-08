def majorityElement(self, A, N):
    first=None
    count=0

    for i in range(0,len(A)):
        if A[i]==first:
            count+=1
        elif count==0:
            first=A[i]
            count+=1
        else:
            count-=1
            
    count=0
    for j in range(len(A)):
        if A[j]==first:
            count+=1
            
    if count>N/2:
        return first
    else:
        return -1