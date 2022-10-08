def smallest(root,k,arr):
    if root is None:
        return None
    
    smallest(root.left,k,arr)
    arr.append(root.data)
    smallest(root.right,k,arr)
    


class Solution:
    # Return the Kth smallest element in the given BST 
    def KthSmallestElement(self, root, k): 
        if root is None:
            return -1
        arr=[]
        smallest(root,k,arr)
        i=0
        while i<len(arr) and i<=k-1:
            if i==k-1:
                return arr[i]
            i+=1
        return -1