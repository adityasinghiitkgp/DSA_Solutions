def height(self, root):
    if not root:
        return 0
    l=self.height(root.left)
    r=self.height(root.right)
    return max(l,r)+1