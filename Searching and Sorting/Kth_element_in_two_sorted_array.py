def kthElement(self,  arr1, arr2, n, m, k):
    i=0
    j=n-1
    while i<m and j>0:
        if arr1[j]>=arr2[i]:
            arr1[j],arr2[i]=arr2[i],arr1[j]
            i+=1
            j-=1
        else:
            break
    arr1.sort()
    arr2.sort()
    
    if k<=n:
        return arr1[k-1]
    else:
        return arr2[k-n-1]