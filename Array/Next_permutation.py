def nextPermutation(nums):
    just_big=-1
    swap=-1
    for i in range(len(nums)-1,0,-1):
        if nums[i]>nums[i-1]:
            just_big=i
            swap=i-1
            break
    if just_big==-1:
        nums[:]=nums[-1::-1]
        return nums
    for i in range(just_big,len(nums)):
        if nums[i]>nums[swap] and nums[i]<=nums[just_big]:
            just_big=i
    
    nums[just_big],nums[swap]=nums[swap],nums[just_big]
    
    x=nums[0:swap+1]
    y=nums[swap+1:]
    y=y[-1::-1]
    nums[:]=x+y
    return nums
        