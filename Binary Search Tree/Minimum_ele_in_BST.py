def minValue(root):
    if root is None:
        return root
    if root.left is None:
        return root.data
    return minValue(root.left)