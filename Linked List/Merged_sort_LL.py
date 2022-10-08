    
    
def sortedmerge(a,b):    
    res=None
    if a==None:
        return b
    elif b==None:
        return a
    
    if a.data>b.data:
        res=b
        res.next=sortedmerge(a,b.next)
    else:
        res=a
        res.next=sortedmerge(a.next,b)
    
    return res

def middle(head):
    slow=head
    fast=head
    while fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next
    return slow
    
class Solution:
    #Function to sort the given linked list using Merge Sort.
    def mergeSort(self, head):
        
        if head==None or head.next==None:
            return head
            
        middle_ele=middle(head)
        next_middle=middle_ele.next
        middle_ele.next=None
        
        left=self.mergeSort(head)
        right=self.mergeSort(next_middle)
        x=sortedmerge(left,right)
        return x
        
        