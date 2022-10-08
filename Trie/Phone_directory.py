def displayContacts(self, n, contacts, s):
    

    contacts.sort()
    query=s
    ans=[]
    i=1
    
    while i< len(query)+1:
        flag=False
        li=[]
        
        for contact in contacts:
            if contact.startswith(query[0:i]):
                flag=True
                if contact not in li:
                    li.append(contact)
                

        if flag==False:
            li.append("0")
        
        ans.append(li)
            
        i+=1
    return ans