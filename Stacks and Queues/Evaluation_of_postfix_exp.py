def evaluatePostfix(self, S):
    num=[]
    exp=[]
    for i in S:
        if i.isnumeric():
            num.append(i)
        
        else:
            
            if len(num)>1:
                val1=int(num.pop())
                val2=int(num.pop())
                if i=="*":
                    num.append(int(val1*val2))
                elif i=="+":
                    num.append(int(val1+val2))
                elif i=="%":
                    num.append(int(val2%val1))
                elif i=="-":
                    num.append(int(val2-val1))
                else:
                    num.append(int(val2/val1))
                    
    return num[0]