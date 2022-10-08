
class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        zero=0
        one=0
        two=0
        curr=head
        while curr:
            if curr.data==0:
                zero+=1
            elif curr.data==1:
                one+=1
            else:
                two+=1
            curr=curr.next
        
        curr=head
        while curr:
            if zero>0:
                curr.data=0
                zero-=1
            elif one>0:
                curr.data=1
                one-=1
            else:
                curr.data=2
                two-=1
            curr=curr.next
            
        return head