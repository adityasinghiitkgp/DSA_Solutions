def solve(root,low,high):
    if not root:
        return 0
    count=0
    if root.data==low and root.data==high:
        return 1
    if root.data>=low and root.data<=high:
        return count+1+solve(root.left,low,high)+solve(root.right,low,high)
    elif root.data>low:
        return count+solve(root.left,low,high)
    else:
        return count+solve(root.right,low,high)        

        
#Function to count number of nodes in BST that lie in the given range.

class Solution:
    def getCount(self,root,low,high):
        count=0
        count+=solve(root,low,high)
        return count