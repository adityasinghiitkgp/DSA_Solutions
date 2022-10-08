def countSquares(self, N):
    x=N**0.5
    if int(x)<x:
        x+=1
    return int(x-1)