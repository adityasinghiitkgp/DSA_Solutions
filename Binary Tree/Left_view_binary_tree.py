def solve(root,ans,level,d):
    if not root:
        return 
    if level not in d:
        ans.append(root.data)
        d[level]=1
    solve(root.left,ans,level+1,d)
    solve(root.right,ans,level+1,d)
    
#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    ans=[]
    level=0
    d={}
    solve(root,ans,level,d)
    return ans
    # code here