def solve(nums,target,l,r):
    if l>r:
        return -1
    mid=(l+r)//2
    
    if target==nums[mid]:
        return mid
    if nums[l]<=nums[mid]:
        if target>=nums[l] and target<=nums[mid]:
            return solve(nums,target,l,mid-1)
        return solve(nums,target,mid+1,r)
    else:
        if nums[r]>=target and nums[mid]<=target:
            return solve(nums,target,mid+1,r)
        return solve (nums,target,l,mid-1)

class Solution:
    def search(self, nums, target):
        l=0
        r=len(nums)-1
        return solve(nums,target,l,r)