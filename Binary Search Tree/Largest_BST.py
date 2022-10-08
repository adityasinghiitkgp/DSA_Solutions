def size(root):
    if not root:
        return 0
    l=size(root.left)
    r=size(root.right)
    return l+r+1
def check(root,l,r):
    if not root:
        return True
    if l!=None and root.data<=l:
        return False
    if r!=None and root.data>=r:
        return False
    
    if check(root.left,l,root.data) and check(root.right,root.data,r):
        return True
    return False
    
class Solution:
    # Return the size of the largest sub-tree which is also a BST
    def largestBst(self, root):
        if check(root,None,None):
            return size(root)
        return max(self.largestBst(root.left),self.largestBst(root.right))