def getfactors():
    #num=raw_input("����һ�����֣�")
    num=45
    con=num
    a=[]
    while con>0:
        
        if num % con == 0:
            a.append(con)
        con -=1
           
    print a
if __name__=='__main__':
    getfactors()