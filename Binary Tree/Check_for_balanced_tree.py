def height(root):
    if root is None:
        return 0
    else:
        l=height(root.left)
        r=height(root.right)
        if l>r:
            return l+1
        else:
            return r+1

#Function to check whether a binary tree is balanced or not.
class Solution:
    def isBalanced(self,root):
        if not root:
            return True
        
        l=height(root.left)
        r=height(root.right)
        if abs(l-r)<2 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False
        