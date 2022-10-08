class Solution:
    def divide(self, N, head):
        odd=[]
        even=[]
        curr=head
        while curr:
            if curr.data%2==0:
                even.append(curr.data)
            else:
                odd.append(curr.data)
            curr=curr.next
        
        curr=head
        i=0
        j=0
        while curr:
            if i<len(even):
                curr.data=even[i]
                i+=1
            elif j<len(odd):
                curr.data=odd[j]
                j+=1
            curr=curr.next
        return head