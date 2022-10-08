def PalinArray(arr ,n):
    for i in range(n):
        
        lis=list(map(str,arr))
        rev=lis[i]
        if lis[i]!= rev[-1::-1]:
            
            return False
    return True