def solve(root):
    if not root:
        return 0,0,0
    max_node=0
    sumi=root.data
    dis=0
    n1,s1,d1=solve(root.left)
    n2,s2,d2=solve(root.right)
    if d1>d2:
        max_node=n1
        sumi+=s1
        dis=d1+1
    else:
        max_node=n2
        sumi+=s2
        dis=d2+1
    
    return max_node,sumi,dis
    
class Solution:
    def sumOfLongRootToLeafPath(self,root):

        max_node,dis,sumi=solve(root)
        return dis