def productExceptSelf(self, nums, n):
    lis=[]
    for i in range(n):
        if nums[i]==0:
            lis.append(i)
    
    if len(lis)>1:
        return [0]*n
        
    if len(lis)==1:
        ans=[]
        pro=1
        for i in range(n):
            if i!=lis[0]:
                pro*=nums[i]
        
        for i in range(n):
            if i!=lis[0]:
                ans.append(0)
            else:
                ans.append(pro)
    
    else:
        pro=1
        ans=[]
        for i in range(n):
            pro*=nums[i]
        for i in range(n):
            ans.append(pro//nums[i])
    return ans