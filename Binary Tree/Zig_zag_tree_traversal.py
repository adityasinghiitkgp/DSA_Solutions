def zigZagTraversal(self, root):
    arr=[]
    arr.append(root)
    ans=[]
    flag=True
    while arr:
        n=len(arr)
        if flag:
            for i in range(n):
                ans.append(arr[i].data)
        else:
            for i in range(n-1,-1,-1):
                ans.append(arr[i].data)
        for i in range(n):
            x=arr.pop(0)
            if x.left:
                arr.append(x.left)
            if x.right:
                arr.append(x.right)
        flag=not flag
    return ans