class MyQueue:
    
    def __init__(self):
        self.arr=[]
        
    def push(self, x):
        self.arr.append(x)
        
     
    #Function to pop an element from queue and return that element.
    def pop(self): 
        if self.arr:
            x=self.arr.pop(0)
            return x
    
        return -1