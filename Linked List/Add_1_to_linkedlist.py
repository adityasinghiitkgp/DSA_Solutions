

def reverse(head):
    prev=None
    current=head
    while current:
        new=current.next
        current.next=prev
        prev=current
        current=new
    return prev

class Solution:
    def addOne(self,head):
        carry=0
        
        head=reverse(head)
        k=head
        head.data+=1
        prev=None
        
        while head!=None and (carry>0 or head.data>9):
            prev=head
            head.data+=carry
            carry=head.data//10
            head.data=head.data%10
    
            head=head.next
        if carry>0:
            new=Node(carry)
            prev.next=new

        head=reverse(k)
        return head