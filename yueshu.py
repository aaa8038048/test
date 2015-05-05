def getfactors():
    #num=raw_input("输入一个数字：")
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