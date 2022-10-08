


#Function to push an integer into the stack1.
def push1(a,x):
    global top2,top1
    a[top1+1]=x
    top1+=1
    
#Function to push an integer into the stack2.
def push2(a,x):
    global top2,top1
    a[top2-1]=x
    top2-=1
    
#Function to remove an element from top of the stack1.    
def pop1(a):
    global top2,top1
    if top1!=-1:
        top1-=1
        return a[top1+1]
    return -1
    
#Function to remove an element from top of the stack2.    
def pop2(a):
    global top2,top1
    if top2!=101:
        top2+=1
        return a[top2-1]
    return -1
    #code here
    