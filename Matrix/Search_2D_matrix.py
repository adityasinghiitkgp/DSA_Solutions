def searchMatrix(self,matrix,target):
    pos=0
    for i in range(len(matrix)):
        if target<=matrix[i][len(matrix[0])-1]:
            pos=i
            break
    
    for i in range(len(matrix[0])):
        if target==matrix[pos][i]:
            return True
    return False