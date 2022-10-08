#Function that constructs BST from its preorder traversal.
def post(root,lis):
    if not root:
        return
    post(root.right,lis)
    post(root.left,lis)
    lis.append(root.data)
def solve(inor,pre):
    if not pre:
        return 
    root=pre[0]
    idx=inor.index(root)
    root=Node(root)
    root.left=solve(inor[:idx+1],pre[1:idx+1])
    root.right=solve(inor[idx+1:],pre[idx+1:])
    return root

class Node:

    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

#Function that constructs BST from its preorder traversal.
def post_order(pre, size):
    inor=sorted(pre)
    root=solve(inor,pre)
    return root
