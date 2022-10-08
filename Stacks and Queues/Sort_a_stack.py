def insert(stack,item):
    if not stack:
        stack.append(item)
    else:
        if stack[-1]<item:
            temp=stack.pop()
            insert(stack,item)
            stack.append(temp)
        else:
            stack.append(item)

def sorted(s):
    if s:
        temp=s.pop()
        sorted(s)
        
        insert(s,temp)
    return s