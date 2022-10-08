def minJumps(self, arr, n):
    if arr[0]==0:
        return -1
        
    maxi=arr[0]
    step=arr[0]
    jump=1
    for i in range(1,n):
        if i==n-1:
            return jump

        maxi=max(maxi,i+arr[i])
        step-=1
        if step==0:
            jump+=1
            if i>=maxi:
                return -1
            step=maxi-i
    