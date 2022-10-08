def find(arr,n,x):
    first=-1
    last=-1
    flag=True
    for i in range(n):
        if arr[i]==x:
            if flag==True:
                first=i
                flag=False
            last=i
    return (first,last)
