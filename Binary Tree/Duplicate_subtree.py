def solve(root,d,res):
    
    if root is None:
        return 
    s="("
    s+=str(root.data)
    s+=str(solve(root.left,d,res))
    s+=str(solve(root.right,d,res))
    s+=")"
    
    
    if s in d.keys():
        d[s]+=1
        if d[s]==2:
            res.append(root)
    else:
        d[s]=1
    return s
        

class Solution:
    def printAllDups(self,root):
        res=[]
        d={}
        curr=[]
        solve(root,d,res)
        return res