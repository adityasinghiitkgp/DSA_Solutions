def solve(lis,root,level,first):
    if root is None:
        return 
    if first[0]<level:
        lis.append(root.data)
        first[0]=level
        
    solve(lis,root.right,level+1,first)
    solve(lis,root.left,level+1,first)
    return lis
    
class Solution:
    #Function to return list containing elements of right view of binary tree.
    def rightView(self,root):
        if root is None:
            return []
        lis=[]
        first=[0]
        level=1
        return solve(lis,root,level,first)