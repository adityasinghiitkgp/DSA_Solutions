def path(root,n,p):
    if not root:
        return False
    p.append(root)
    if root.data==n:
        return True
    
    if path(root.left,n,p) or path(root.right,n,p):
        return True
    p.pop()
    return False
class Solution:
    #Function to return the lowest common ancestor in a Binary Tree.
    def lca(self,root, n1, n2):
        path1=[]
        path2=[]
        path(root,n1,path1)
        path(root,n2,path2)
        if len(path1)==0 or len(path2)==0:
            return Node(-1)
        i=0
        while i<len(path1) and i<len(path2):
            if path1[i]!=path2[i]:
                break
            i+=1

        return path1[i-1]
        
            