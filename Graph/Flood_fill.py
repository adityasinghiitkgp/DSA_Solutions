
def solve(visited,sr,sc,new,image,row,col,same):
    if  sr<0 or sr>=row or sc<0 or sc>=col or visited[sr][sc] or image[sr][sc]!=same:
        return False
    visited[sr][sc]=True
    if image[sr][sc]==same:
        image[sr][sc]=new
    
    solve(visited,sr-1,sc,new,image,row,col,same)
    solve(visited,sr+1,sc,new,image,row,col,same)
    solve(visited,sr,sc-1,new,image,row,col,same)
    solve(visited,sr,sc+1,new,image,row,col,same)

class Solution:
    def floodFill(self, image,sr,sc,newColor):
        row=len(image)
        col=len(image[0])
        same=image[sr][sc]
        visited=[[False for i in range(col)]for j in range(row)]
        solve(visited,sr,sc,newColor,image,row,col,same)
        return image