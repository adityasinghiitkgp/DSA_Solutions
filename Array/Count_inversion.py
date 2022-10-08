
def countinver(arr, temp,left,right):
    count=0
    if left<right:
        mid=(left+right)//2
        count+=countinver(arr,temp,left,mid)
        count+=countinver(arr,temp,mid+1,right)
        count+=merge(arr,temp,left,mid,right)
    return count

def merge(arr,temp,left,mid,right):
    i=left
    j=mid+1
    k=left
    count=0
    while i<=mid and j<= right:
        if arr[i]>arr[j]:
            temp[k]=arr[j]
            j+=1
            k+=1
            count+=mid-i+1
        else:
            temp[k]=arr[i]
            i+=1
            k+=1

    while i<=mid:
        temp[k]=arr[i]
        i+=1
        k+=1
    while j<=right:
        temp[k]=arr[j]
        j+=1
        k+=1
    
    for loop_var in range(left, right + 1): 
        arr[loop_var] = temp[loop_var]

    return count
    
class Solution:
    def inversionCount(self, arr, n):
    
        temp=[0]*n
        return countinver(arr,temp,0,n-1)