def factorial(self, N):
    fact=1
    for i in range(1,N+1):
        fact=fact*i
    lis=[]
    lis.append(fact)
    return lis