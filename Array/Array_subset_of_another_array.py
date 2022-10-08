def isSubset( a1, a2, n, m):
    lis1=list(set(a1))
    lis2=list(set(a2))
    for i in range(m):
        if lis2[i] not in lis1:
            return "No"
    return "Yes"
    
    