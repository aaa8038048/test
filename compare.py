import keyword
def Comparestr():
    str1=raw_input('输入需要判断的第一个字符串')
    str2=raw_input('请输入需要判断的第二个字符串')
    len1=len(str1)
    len2=len(str2)
    if len1>len2:
        print '第一个字符串较长'
    if len2>len1:
        print '第二个字符串较长'
    if len1==len2:
        print '两个字符串一样长'
def Iskeyword():
    str=raw_input('输入需要判断的字符串')
    if keyword.iskeyword(str):
        print '是关键字'
    else:
        print '不是关键字'
def Mianmenu():
    pr="""
    (1).比较字符串
    (2).判断是否为关键字
    (3).退出
    请选择:
    
    """
    while True:
        while True:
            try:choice=raw_input(pr).strip()[0].lower()
            except (EOFError,KeyboardInterrupt,IndexError):
                choice='3'
            if choice not in '123':
                print'invalid option,try again'
            else:
                break
        if choice=='1':
            Comparestr()
        if choice=='2':
            Iskeyword()
        if choice=='3':
            break
if __name__=='__main__':
    Mianmenu()