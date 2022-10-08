def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not root:
        return root
    if key>root.val:
        root.right=self.deleteNode(root.right,key)
    elif key<root.val:
        root.left=self.deleteNode(root.left,key)
    else:
        if root.left==None:
            temp=root.right
            root=None
            return temp
        elif root.right==None:
            temp=root.left
            root=None
            return temp
        else:
            temp=miright(root.right)
            root.val=temp.val
            root.right=self.deleteNode(root.right,temp.val)
    return root