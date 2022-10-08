def counter(head):
    temp=head
    count=0
    while temp is not None:
        temp=temp.next
        count+=1
    return count
class Solution:
    def middleNode(self,head):
        slow=head
        fast=head
        while fast.next and fast.next.next:
    
            slow=slow.next
            fast=fast.next.next
        count=counter(head)
        if count%2==0:
            return slow.next
        return slow
        