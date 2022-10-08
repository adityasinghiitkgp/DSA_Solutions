from heapq import heappop,heappush
class Node:
    def __init__(self,ch,freq,left=None,right=None):
        self.ch=ch
        self.freq=freq
        self.left=left
        self.right=right
        
    def __lt__(self,other):
        return self.freq<other.freq


class Solution:
    def huffmanCodes(self,S,f,N):
        # Code here
        pq=[Node(S[i],f[i]) for i in range(N)]
        heapq.heapify(pq)
        while len(pq)!=1:
             left=heappop(pq)
             right=heappop(pq)
             total=left.freq+right.freq
             heappush(pq,Node(None,total,left,right))
        def preorder(n,root):
            nonlocal ans
            if root.left is None and root.right is None:
                   ans.append(n)
            if root.left:
                preorder(n+'0',root.left)
            if root.right:
                 preorder(n+'1',root.right)
            return  
        root=pq[0]
        ans=[]
        preorder('',root)
        return ans
        
        
        