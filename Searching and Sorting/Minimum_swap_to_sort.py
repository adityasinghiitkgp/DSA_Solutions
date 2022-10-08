def minSwaps(self, nums):
    d={}
    arr=[]
    for i in range(len(nums)):
        arr.append([nums[i],i])
    arr.sort()
    ans=0
    visited=[False]*len(nums)
    for i in range(len(nums)):
        if arr[i][1]==i or visited[i]:
            continue
        cycle=0
        j=i
        while not visited[j]:
            visited[j]=True
            cycle+=1
            j=arr[j][1]
        ans+=cycle-1
    return ans