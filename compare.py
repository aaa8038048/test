import keyword
def Comparestr():
    str1=raw_input('������Ҫ�жϵĵ�һ���ַ���')
    str2=raw_input('��������Ҫ�жϵĵڶ����ַ���')
    len1=len(str1)
    len2=len(str2)
    if len1>len2:
        print '��һ���ַ����ϳ�'
    if len2>len1:
        print '�ڶ����ַ����ϳ�'
    if len1==len2:
        print '�����ַ���һ����'
def Iskeyword():
    str=raw_input('������Ҫ�жϵ��ַ���')
    if keyword.iskeyword(str):
        print '�ǹؼ���'
    else:
        print '���ǹؼ���'
def Mianmenu():
    pr="""
    (1).�Ƚ��ַ���
    (2).�ж��Ƿ�Ϊ�ؼ���
    (3).�˳�
    ��ѡ��:
    
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