def countAndSay(self, n: int) -> str:
    if n==1:
        return "1"
    elif n==2:
        return "11"
    
    x="11"
    for i in range(3,n+1):
        x+="$"
        i=0
        count=0
        s=""
        while i <len(x)-1:
            if x[i]==x[i+1]:
                count+=1
            else:
                s+=str(count+1)+str(x[i])
                count=0
            i+=1

        x=s
        
    return x