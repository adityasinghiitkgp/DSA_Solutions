def shortest_distance(self, matrix):
    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][k]==-1 or matrix[k][j]==-1:
                    continue
                elif matrix[i][j]==-1:
                    matrix[i][j]=matrix[i][k]+matrix[k][j]
                elif matrix[i][k]+matrix[k][j]<matrix[i][j]:
                    matrix[i][j]=matrix[i][k]+matrix[k][j]