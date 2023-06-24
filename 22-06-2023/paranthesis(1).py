stack=[]
s=input("enter paranthesis")
n=len(s)
flag=1
if s[0]==']' or s[0]=='}' or s[0]==')':
    print(False)
else:
    for i in range(n):
        if s[i]=='[' or s[i]=='(' or s[i]=='{':
            stack.append(s[i])
        elif s[i]==']'or s[i]=='}' or s[i]==')':
            if(s[i]=='}'):
               c=0
               for i in range(len(stack)):
                    if(s[i]=='{'):
                        c+=1
            elif(s[i]==')'):
               c=0
               for i in range(len(stack)):
                    if(s[i]=='('):
                        c+=1
            elif(s[i]==']'):
               c=0
               for i in range(len(stack)):
                    if(s[i]=='['):
                        c+=1
            else:
              flag=0
              break
        else:
            flag=-1
            break
    if flag==1 and c==1:
        print(True)
    elif flag==0 :
        print(False)
    else:
        print("Invalid paranthesis")
