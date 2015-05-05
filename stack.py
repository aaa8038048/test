stack=[]

def pushit():
    stack.append(raw_input('Enter your choice:').strip())
def popit():
    if len(stack)==0:
        print 'this is an empty stack'
    else:
        stack.pop()
    
def viewstack():
    print stack
CMDs={'u':pushit,'o':popit,'v':viewstack}
def showmenu():
    pr="""
U:push-
O:pop-
V:view-
Q:qiot-
Enter choice:
    """
    while True:
        while True:
            try:
                choice=raw_input(pr).strip()[0].lower()
            except (EOFError,KeyboardInterrupt,IndexError):
                choice='q'
            if choice not in 'uovq':
                print'invalid option,try again'
            else:
                break
        if choice=='q':
            break
        CMDs[choice]()
if __name__=='__main__':
    showmenu()
            
