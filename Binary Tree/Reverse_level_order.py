
def reverseLevelOrder(root):
    ans=[]
    lis=[]
    lis.append(root)
    while lis:
        x=lis.pop(0)
        ans.append(x.data)
        if x.right:
            lis.append(x.right)
        if x.left:
            lis.append(x.left)
    return ans[::-1]