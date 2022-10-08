#Function to push an element into stack using two queues.
def push(x):
    
    # global declaration
    global queue_1
    global queue_2
    queue_1.append(x)
    while queue_2:
        queue_1.append(queue_2.pop(0))
    queue_1,queue_2=queue_2,queue_1


#Function to pop an element from stack using two queues.     
def pop():
    
    # global declaration
    global queue_1
    global queue_2
    if queue_2:
        return queue_2.pop(0)
    return -1
    # code here