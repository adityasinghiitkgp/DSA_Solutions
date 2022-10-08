#User function Template for python3
def solve(x):
    count=0
    while x>0:
        x=(x & (x-1))
        count+=1
    return count

class Solution:
    ##Complete this function
    # Function to find number of bits needed to be flipped to convert A to B
    def countBitsFlip(self,a,b):
        x=(a^b)
        count=solve(x)
        return count
