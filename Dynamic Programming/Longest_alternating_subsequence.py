def AlternatingaMaxLength(self, nums):
    inc=1
    dec=1
    n=len(nums)
    for i in range(1,n):
        if nums[i-1]>nums[i]:
            dec=inc+1
        elif nums[i]>nums[i-1]:
            inc=dec+1
    return max(inc,dec)