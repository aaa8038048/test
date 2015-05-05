import sys
import random
dic={1:"石头",2:"剪刀",3:"布"}
def game(player):
    robot=random.randint(1,3)
    if player==robot:
        print "你们平局，电脑是 %s，你是 %s" % (dic[robot],dic[player])
    if player%3+1==robot:
        print "你赢了，电脑是 %s，你是 %s" % (dic[robot],dic[player])
    if robot%3+1==player:
        print "电脑赢了，电脑是 %s，你是 %s" % (dic[robot],dic[player])
def view():
    print "游戏规则：输入1为石头，2为剪刀，3为布，输入quit退出："
    while True:
        try:
            player=raw_input("请输入数字:")
        except(EOFError,KeyboardInterrupt,IndexError):
            player='quit'
        if not player.isdigit():  
            print("请输入数字")  
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