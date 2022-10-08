def singleNumber(self, nums):
    res=[]
    xor=0
    sum1=0
    sum2=0
    for i in range(len(nums)):
        xor^=nums[i]
    
    xor=(xor & -xor)
    
    for i in range(len(nums)):
        if (xor & nums[i])>0:
            sum1=(sum1^nums[i])
        else:
            sum2=(sum2^nums[i])
    
    res.append(sum1)
    res.append(sum2)
    res.sort()
    return res