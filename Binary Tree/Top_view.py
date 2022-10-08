

def solve(root,level,order,d):
    if not root:
        return 
    if level not in d:
        d[level]=[root.data,order]
    else:
        if d[level][1]>order:
            d[level]=[root.data,order]
    if root.left:
        solve(root.left,level-1,order+1,d)
    if root.right:
        solve(root.right,level+1,order+1,d)
    

        

class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        if not root:
            return

        d={}
        solve(root,0,0,d)
        x=sorted(d.keys())
        ans=[]
        for i in x:
            ans.append(d[i][0])
        return ans