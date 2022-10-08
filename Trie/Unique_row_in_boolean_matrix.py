def uniqueRow(row, col, mat):
    index=0
    matrix=[[0 for x in range (col)] for y in range(row)]
    for i in range(row):
        for j in range(col):
            matrix[i][j]=mat[index]
            index+=1
    
    arr = []
    for i in range(row):
        k =""
        mat = []
        for j in range(col):
            k+=str(matrix[i][j])
            if j<col-1:
                k+=" "
        
        mat.append(k)
        

        if mat not in arr:
            arr.append(mat)

        
    return arr