def rev(q):
    arr=[]
    while not q.empty():
        x=q.get()
        arr.append(x)
    while arr:
        q.put(arr[-1])
        arr.pop()
        
    return q