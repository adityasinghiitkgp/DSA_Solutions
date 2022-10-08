def fractionalknapsack(self, W,Items,n):
    
    lis=[]
    for i in range(len(Items)):
        lis.append([Items[i].value/Items[i].weight,Items[i].value,Items[i].weight])
    lis.sort(reverse=True)
    sumi=0
    i=0
    
    while W and i<len(lis):
        if lis[i][2]<=W:
            W-=lis[i][2]
            sumi+=lis[i][1]
            i+=1
        else:
            sumi+=(W*lis[i][0])
            W=0
    return sumi