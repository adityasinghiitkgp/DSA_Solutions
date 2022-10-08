
def heapify(arr,n,i):
    large=i
    l=i*2+1
    r=i*2+2
    if l<n and arr[l]>arr[large]:
        large=l
    if r<n and arr[r]> arr[large]:
        large=r
        
    if large!=i:
        arr[large],arr[i]=arr[i],arr[large]
        heapify(arr,n,large)
        
def buildheap(arr,n):
    index=n//2-1
    for i in range(index,-1,-1):
        heapify(arr,n,i)
        
class Solution():
    def mergeHeaps(self, a, b, n, m):
        arr=[0]*(n+m)
        for i in range(n):
            arr[i]=a[i]
        for i in range(m):
            arr[i+n]=b[i]
        buildheap(arr,n+m)
        return arr