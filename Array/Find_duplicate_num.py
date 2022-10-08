def findDuplicate(nums):
    s=set()
    for i in range(len(nums)):
        size=len(s)
        s.add(nums[i])
        new=len(s)
        if new==size:
            return nums[i]
    return -1