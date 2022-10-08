def sort012(self,arr,n):
    count0=0
    count1=0
    count2=0
    for i in arr:
        if i==0:
            count0+=1
        elif i==1:
            count1+=1
        else:
            count2+=1
    
    for i in range(len(arr)):
        if count0!=0:
            arr[i]=0
            count0-=1
        elif count1!=0:
            arr[i]=1
            count1-=1
        else:
            arr[i]=2
    return arr
