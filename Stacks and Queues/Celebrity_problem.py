def celebrity(self, M, n):
    row=-1
    for i in range(n):
        if sum(M[i])==0:
            row=i
            break
    if row==-1:
        return row
    for i in range(n):
        if M[i][row]==0 and i!=row:
            return -1
    return row