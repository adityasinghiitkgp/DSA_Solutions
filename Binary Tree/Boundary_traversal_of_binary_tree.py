

def print_left(root,res):
    if root:
        if root.left:
            res.append(root.data)
            print_left(root.left,res)
        elif root.right:
            res.append(root.data)
            print_left(root.right,res)

def print_right(root,res):
    if root:
        if root.right:
            print_right(root.right,res)
            res.append(root.data)
           
        elif root.left:
            print_right(root.left,res)
            res.append(root.data)
            

def leave(root,res):
    if root:
        leave(root.left,res)
        if root.left==None and root.right==None:
            res.append(root.data)
        leave(root.right,res)
    

class Solution:
    def printBoundaryView(self,root):
        res=[]
        if root:
            res.append(root.data)
            print_left(root.left,res)
            leave(root.left,res)
            leave(root.right,res)
            print_right(root.right,res)
            
            
        return res