l=input("enter parnthesies")
c=0
for i in range(len(l)):
    if(('()'in l) and ('[]' in l) and ( '{}' in l)):
         c+=1 
    if('(' in l):
        if(')' in l):
                c+=1
    if('[' in l):
        if(']' in l):
                    c+=1
    if('{' in l):
        if('}' in l):
                   c+=1
    else:
        c=0
if(c>=1):
    print("valid")
else:
    print("invalid")
    