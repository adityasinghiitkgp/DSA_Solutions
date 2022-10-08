def sumi(root):
    if not root:
        return 0
    l=sumi(root.left)
    r=sumi(root.right)
    return l+r+root.data
    
class Solution:
    def isSumTree(self,root):
        if not root or (not root.left and not root.right):
            return True

        l=sumi(root.left)
        r=sumi(root.right)
        if root.data==l+r and self.isSumTree(root.left) and self.isSumTree(root.right):
            return True
        return False
