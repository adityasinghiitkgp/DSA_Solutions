def solve(inorder,preorder,n):
    if not preorder:
        return
    root=(preorder[0])
    idx=inorder.index(root)
    root=Node(root)
    root.left=solve(inorder[:idx],preorder[1:idx+1],n)
    root.right=solve(inorder[idx+1:],preorder[idx+1:],n)
    return root
class Solution:
    def buildtree(self, inorder, preorder, n):
        return solve(inorder,preorder,n)