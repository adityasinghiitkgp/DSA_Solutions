def isHeap(self, root):
    not_seen=False
    arr=[]
    arr.append(root)
    while arr:
        root=arr.pop(0)
        if root.left:
            if not_seen or root.data<=root.left.data:
                return False
            arr.append(root.left)
        else:
            not_seen=True
            
        if root.right:
            if not_seen or root.data<=root.right.data:
                return False
            arr.append(root.right)
    return True
                