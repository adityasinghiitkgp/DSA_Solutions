def findLongestConseqSubseq(self,arr, N):
    arr=sorted(set(arr))
    N=len(arr)
    maxi=-10**9
    temp=arr[0]
    curr=1
    for i in range(1,N):
        if temp+1==arr[i]:
            curr+=1
            temp+=1
        else:
            if curr>maxi:
                maxi=curr
            curr=1
            temp=arr[i]
    if maxi<curr:
        maxi=curr
    return maxi