
# function should append an element on to the stack
def push(arr, ele):
    arr.append(ele)
    

# Function should pop an element from stack
def pop(arr):
    if arr:
        arr.pop()
   

# function should return 1/0 or True/False
def isFull(n, arr):
    if len(arr)==n:
        return True
    return False

# function should return 1/0 or True/False
def isEmpty(arr):
    if len(arr)==0:
        return True
    return False

# function should return minimum element from the stack
def getMin(n, arr):
    mini=arr[0]
    for i in arr:
        if mini>i:
            mini=i
    return mini