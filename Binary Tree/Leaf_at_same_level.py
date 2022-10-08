

def checklevel(root,d,level):
    if root is None:
        return 
    
    if root.left==None and root.right==None:
        if level in d.keys():
            d[level]+=1
        else:
            d[level]=1
        
    if root.left:   
        checklevel(root.left,d,level+1)
    if root.right:
        checklevel(root.right,d,level+1)

class Solution:
    #Your task is to complete this function
    #function should return True/False or 1/0
    def check(self, root):
        if root is None:
            return 1 
        d={}
        level=0
        checklevel(root,d,level)
        if len(d)>1:
            return False
        return True
