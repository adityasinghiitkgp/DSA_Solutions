def LCA(root, n1, n2):
    if not root:
        return Node(-1)
    if root.data>n1 and root.data>n2:
        return LCA(root.left,n1,n2)
    elif root.data<n1 and root.data<n2:
        return LCA(root.right,n1,n2)
    else:
        return root