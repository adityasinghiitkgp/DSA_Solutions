def modifyQueue(q,k):
    if k>=len(q):
        return q[-1::-1]
    else:
        q=q[k-1::-1]+q[k:]
        return q