def levelOrder(self,root ):
    lis=[]
    ans=[]
    lis.append(root)
    while lis:
        x=lis.pop(0)
        ans.append(x.data)
        if x.left:
            lis.append(x.left)
        if x.right:
            lis.append(x.right)
            
    return ans