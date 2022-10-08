def maxSubArraySum(self,arr,N):
    maxi=arr[0]
    curr=arr[0]
    for i in range(1,N):
        curr=max(arr[i],arr[i]+curr)
        maxi=max(maxi,curr)
    return maxi