import sys
import random
dic={1:"ʯͷ",2:"����",3:"��"}
def game(player):
    robot=random.randint(1,3)
    if player==robot:
        print "����ƽ�֣������� %s������ %s" % (dic[robot],dic[player])
    if player%3+1==robot:
        print "��Ӯ�ˣ������� %s������ %s" % (dic[robot],dic[player])
    if robot%3+1==player:
        print "����Ӯ�ˣ������� %s������ %s" % (dic[robot],dic[player])
def view():
    print "��Ϸ��������1Ϊʯͷ��2Ϊ������3Ϊ��������quit�˳���"
    while True:
        try:
            player=raw_input("����������:")
        except(EOFError,KeyboardInterrupt,IndexError):
            player='quit'
        if not player.isdigit():  
            print("����������")  
            continue  
        if player=='quit':
            break
        ichoice = int(player)
        if ichoice >= 1 and ichoice <= 3:  
            game(ichoice)  
        else:  
            print("please input the number between 1 and 3")         
         
         
         
if __name__=="__main__":
    view()