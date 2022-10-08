

def inorder(root,res):
    if root is None:
        return 
    inorder(root.left,res)
    res.append(root.data)
    inorder(root.right,res)
    
def fill(root,res):
    if root is None:
        return
    fill(root.left,res)
    root.data=res[0]
    res.pop(0)
    fill(root.right,res)
    return root
    

class Solution:
    # The given root is the root of the Binary Tree
    # Return the root of the generated BST
    def binaryTreeToBST(self, root):
        res=[]
        inorder(root,res)
        res.sort()
        return fill(root,res)