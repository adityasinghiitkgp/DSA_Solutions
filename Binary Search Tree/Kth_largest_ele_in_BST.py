def inorder(root,res):
    if root is None:
        return 
    inorder(root.left,res)
    res.append(root.data)
    inorder(root.right,res)
    
class Solution:
    def kthLargest(self,root, k):
        res=[]
        inorder(root,res)
        x=len(res)-k
        return res[x]