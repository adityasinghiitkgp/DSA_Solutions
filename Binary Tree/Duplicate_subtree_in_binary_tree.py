def solve(root,d):
    
    if root is None:
        return ""
    s="("
    if not root.left and not root.right:
        s+=str(root.data)
        return s
    
    s+=str(root.data)
    s+=str(solve(root.left,d))
    s+=str(solve(root.right,d))
    s+=")"
    if s not in d:
        d[s]=1
    else:
        d[s]+=1
    return s
    
    
class Solution:
    def dupSub(self, root):
        d={}
        solve(root, d)
        for k,v in d.items():
            if v>1:
                return 1
        return 0
