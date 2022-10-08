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
    def findDist(self,root,a,b):
        path1=[]
        path2=[]
        path(root,a,path1)
        path(root,b,path2)
        if len(path1)==0 or len(path2)==0:
            return 0
        i=0
        while i<len(path1) and i<len(path2):
            if path1[i]!=path2[i]:
                break
            i+=1
        return len(path1)+len(path2)-2*i