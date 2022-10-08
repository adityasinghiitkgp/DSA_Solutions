def solve(root,l,r):
    if not root:
        return False
    if l!=None  and r!=None and r-l==2:
        return True
    if solve(root.left,l,root.data) or solve(root.right,root.data,r):
        return True
    return False
def isdeadEnd(root):
    if solve(root,0,10**9):
        return True
    return False