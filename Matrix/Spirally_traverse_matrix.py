def spirallyTraverse(self,arr, r, c): 
        k=0 
        l=0 
        i=0
        while k<r and l<c:
            for i in range(l,c):
                print(arr[k][i],end=" ")
            k+=1
            for i in range(k,r):
                print(arr[i][c-1],end=" ")
            c-=1
    
            if k<r:
                for i in range(c-1,l-1,-1):
                    print(arr[r-1][i],end=" ")
                r-=1
            if l<c:
                for i in range(r-1,k-1,-1):
                    print(arr[i][l],end=" ")
                l+=1    
        return ""