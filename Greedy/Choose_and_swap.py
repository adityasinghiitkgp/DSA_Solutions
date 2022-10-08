def chooseandswap (self, A):

    lis=[]
    s=set(A)
    for i in s:
        lis.append([ord(i),i])
    lis=sorted(lis)
    j=0
    ans=[]
    i=0
    while i<len(A) and j<len(lis):
        if A[i]!=lis[j][1] and A[i] not in ans:
            temp=A[i]
            A=A.replace(A[i],"@")
            A=A.replace(str(lis[j][1]),temp)
            A=A.replace("@",str(lis[j][1]))
            break
        elif A[i] in ans:
            i+=1
            continue
        else:
            ans.append(A[i])  
            i+=1
            j+=1
    return A