def solve(root,l,r):
    if not root:
        return 1
    if l!=None and l>=root.data:
        return 0
    if r!=None and r<=root.data:
        return 0
    if solve(root.left,l,root.data) and solve(root.right,root.data,r):
        return 1
    return 0
class Solution:
    
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        return solve(root,None,None)