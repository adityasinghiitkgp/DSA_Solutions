import heapq

def get(move,N):
    quot=(move-1)//N
    rem=(move-1)%N
    
    row=N-1-quot
    if quot%2!=0:
        col=N-1-rem
    else:
        col=rem
    return row,col
class Solution:
    def snakesAndLadders(self, board):
        N=len(board)
        lis=[(0,1)]
        heapq.heapify(lis)
        not_seen=set()
        not_seen.add(1)
        while lis:
            dist,ele=heapq.heappop(lis)
            if ele==N*N:
                return dist
            for move in range(ele+1,min(ele+6,N*N)+1):
                row,col=get(move,N)
                
                if board[row][col]!=-1:
                    move=board[row][col]
                if move not in not_seen:
                    heapq.heappush(lis,(dist+1,move))
                    not_seen.add(move)
        return -1
                
                