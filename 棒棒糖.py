import random
peo=['赵','钱','孙','李','周']
while 1:
    ch=input("请选择功能：\n1.点名，2.分发棒棒糖，3.退出\n")
    wh=random.randint(0,4)
    if ch=='1':
        print(peo[wh])
    elif ch=='2':
        print(peo[wh],"获得了",random.randint(5,10),"个棒棒糖")
    elif ch=='3':
        break
    else:
        print("请输入正确选项！")
print("退出系统...")