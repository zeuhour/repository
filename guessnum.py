import random,time
num = random.randint(1,10)
# print(num)
i=5
money=5000
print(num)
print("------猜数字游戏------\n您共有5次机会！")
while 1:
    a=input("请输入一个数字（1-10）： ")
    a=int(a)
    i -= 1
    if num==a:
        print("猜对了")
        break
    else:
        money-=500
        if a>num:
            print("猜大了，您还有",i,"次机会，剩余金额：",money)
        else:
            print("猜小了，您还有",i,"次机会，剩余金额：",money)
    if i==0:
        print("game over")
        time.sleep(1000) #break