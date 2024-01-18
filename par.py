def isempty(stk):
    if stk==[]:
        return True
    else:
        return False
    
def push(stk,x):
    stk.append(x)
    top=len(stk)-1
    
def pop(stk):
    if isempty(stk):
        return 'underflow'
    else:
        y=stk.pop()
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1
            return y

def peek(stk):
    if isempty(stk):
        return 'underflow'
    else:
        top=len(stk)-1
        return stk[top]

def display(stk):
    if isempty(stk):
        print('underflow')
        print()
    else:
        print()
        print('stack values')
        for i in stk:
            if len(i)>6:
                print(i,end=' ')
        print('\n\n')

#main
stack=[]
top=None
while True:
    print()
    print('STACK OPERATIONS')
    print('1.PUSH')
    print('2.POP')
    print('3.PEEK')
    print('4.DISPLAY')
    print('0.EXIT')
    ch=int(input("enter choice"))
    if ch==1:
       item=input("enter city name")
       push(stack,item)

    elif ch==2:
        z=pop(stack)
        if z=="underflow":
            print("underflow")
            print()
        else:
            print("popped item is:",z)
            print()
    elif ch==3:
        z=peek(stack)
        if z=="underflow":
            print('underflow')
            print()
        else:
            print('topmost item is :',z)
            print()

    elif ch==4:
        display(stack)

    elif ch==0:
        break
    else:
        print('invalid choice')


        
            
