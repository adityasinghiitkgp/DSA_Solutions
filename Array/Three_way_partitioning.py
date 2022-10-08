def threeWayPartition(self, array, a, b):
    left=0
    right=len(array)-1
    i=0
    while i<=right:
    
        if array[i]<a:
            array[left],array[i]=array[i],array[left]
            left+=1
            i+=1
        elif array[i]>b:
            array[right],array[i]=array[i],array[right]
            right-=1
        else:
            i+=1
    return array