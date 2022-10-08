
def reverse(head):
    curr=head
    pre=None
    while curr:
        new=curr.next
        curr.next=pre
        pre=curr
        curr=new
    return pre
class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        head1=reverse(first)
        head2=reverse(second)
        
        curr1=head1
        curr2=head2
        carry=0
        flag=True
        while curr1 or curr2:
            if curr1:
                s1=curr1.data
            else:
                s1=0
            if curr2:
                s2=curr2.data
            else:
                s2=0
            sumi=s1+s2+carry
            
           
            carry=sumi//10
            sumi=sumi%10
            if curr1:
                curr1=curr1.next
            if curr2:
                curr2=curr2.next
            temp=Node(sumi)
            if flag:
                head=temp
                curr=temp
                flag=False
            else:
                curr.next=temp
                curr=curr.next
        if carry:
            curr.next=Node(carry)
        head=reverse(head)
        return head