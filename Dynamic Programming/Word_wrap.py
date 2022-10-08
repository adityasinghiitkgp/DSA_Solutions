
import sys
class Solution:
    def solveWordWrap(self, nums, k):
        n=len(nums)
        extra_space=[[0 for i in range(n+1)]for j in range(n+1)]
        line_cost=[[0 for i in range(n+1)]for j in range(n+1)]
        total_cost=[0 for i in range(n+1)]
       
        for i in range(1,n+1):
            extra_space[i][i]=k-nums[i-1]
            
            for j in range(i+1,n+1):
                extra_space[i][j]=(extra_space[i][j-1])-nums[j-1]-1
        for i in range(1,n+1):
            for j in range(i,n+1):
                if extra_space[i][j] < 0:
                    line_cost[i][j] =float('inf')
                elif j==n and extra_space[i][j] >= 0:
                    line_cost[i][j] =0
                else:
                    line_cost[i][j]=(extra_space[i][j])**2
        
        for j in range(1,n+1):
            total_cost[j]=float('inf')
            for i in range(1,j+1):
                if (total_cost[i-1]!=float('inf') and line_cost[i][j]!=float('inf') and (total_cost[i-1] + line_cost[i][j] < total_cost[j])):
                    total_cost[j] = total_cost[i-1] + line_cost[i][j]
                    
     
        return total_cost[n]