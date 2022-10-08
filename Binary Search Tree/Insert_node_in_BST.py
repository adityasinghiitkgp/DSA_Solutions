def insert(root, key):
    if not root:
        return Node(key)
    else:
        if key==root.data:
            return root
        elif key>root.data:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root