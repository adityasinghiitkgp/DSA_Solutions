
def search(grid,word,row,col):
    y=[0,-1,-1,-1,0,1,1,1]
    x=[1,1,0,-1,-1,-1,0,1]

    for i in range(8):
        X=x[i]+row
        Y=y[i]+col
        k=1
        while X>=0 and X<len(grid) and Y>=0 and Y<len(grid[0]) and k<len(word) and grid[X][Y]==word[k]:
            X+=x[i]
            Y+=y[i]
            k+=1
        if k==len(word):
            return True
        else:
            continue
    return False
            
    
class Solution:
    def searchWord(self, grid, word):
        row=len(grid)
        col=len(grid[0])
        ans=[]
        for i in range(row):
            for j in range(col):
                if grid[i][j]==word[0]:
                    if search(grid,word,i,j):
                        move=(i,j)
                        ans.append(move)
        return ans
