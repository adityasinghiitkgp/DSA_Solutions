def toSumTree(self, root) :
    if not root:
        return 0
    pre=root.data
    l=self.toSumTree(root.left)
    r=self.toSumTree(root.right)
    root.data=l+r
    return root.data+pre