def inorder(root,lis):
    if not root:
        return
    inorder(root.left,lis)
    lis.append(root.data)
    inorder(root.right,lis)

#Function to convert a binary tree to doubly linked list.
class Solution:
    def bToDLL(self,root):
        lis=[]
        inorder(root,lis)
        head=Node(lis.pop(0))
        head.left=None
        curr=head
        while lis:
            new=Node(lis.pop(0))
            curr.right=new
            new.left=curr
            curr=curr.right
        return head