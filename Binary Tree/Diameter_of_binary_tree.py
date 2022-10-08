def solve(root,ans):
    if root is None:
        return 0
    
    l=solve(root.left,ans)
    r=solve(root.right,ans)
    temp=max(l,r)+1
    ans[0]=max(ans[0],l+r+1)
    return temp

class Solution:
    
    #Function to return the diameter of a Binary Tree.
    def diameter(self,root):
        ans=[0]
        solve(root,ans)
        return ans[0]