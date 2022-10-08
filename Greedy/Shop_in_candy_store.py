def candyStore(self, candies,N,K):
    maxi=0
    mini=0
    candies=sorted(candies)
    i=0
    j=N-1
    while i<=N-1:
        mini+=candies[i]
        N-=K
        i+=1
    zero=0
    while j>=zero:
        maxi+=candies[j]
        zero+=K
        j-=1
    return [mini,maxi]