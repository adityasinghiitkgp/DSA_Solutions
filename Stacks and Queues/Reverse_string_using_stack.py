def reverse(S):
    a=""
    lis=[]
    for i in S:
        lis.append(i)
    while lis:
        a+=lis.pop()
    return a