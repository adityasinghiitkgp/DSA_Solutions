def solve(root,ans,d,level,order):
    if not root:
        return
    if level not in d:
        d[level]=[root.data,order]
    elif d[level][1]<=order:
        d[level]=[root.data,order]
    solve(root.left,ans,d,level-1,order+1)
    solve(root.right,ans,d,level+1,order+1)
    
class Solution:
    def bottomView(self, root):
        d={}
        ans=[]
        solve(root,ans,d,0,0)
        print
        for k,v in sorted(d.items()):
            ans.append(v[0])
        return ans