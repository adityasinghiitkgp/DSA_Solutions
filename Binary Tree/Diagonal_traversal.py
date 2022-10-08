def diagonal(root):
    lis=[]
    res=[]
    while root:
        res.append(root.data)
        if root.left:
            lis.append(root.left)
        if root.right:
            root=root.right
            
        else:
            if len(lis)>0:
                root=lis.pop(0)
            else:
                root=None
    return res