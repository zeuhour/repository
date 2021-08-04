import random
print("随机选择人物：1.普通 2.稀有（初始30） 3.传奇（不会减少）")
hero=[10,30,10]
a=random.randint(1,3)
print("您的角色是：",a)
score=hero[a-1]
while 1:
    num=[random.randint(1,50),random.randint(1,50),random.randint(1,50)]
    print("请选择数字：\n(1)",num[0],"(2)",num[1],"(3)",num[2])
    ch=input()
#    ch=random.randint(1,3)
    if ch.isdigit():
        ch=int(ch)
    else:
        print("您的输入非法！")
        continue
    co=random.randint(0,1)
    if co == 0 or a==3:
        score+=num[ch-1]
        print("分数增加！您当前分数为：",score)
    else:
        score-=num[ch-1]
        print("分数减少！您当前分数为：",score)
    if score >= 100:
        print("任务成功！")
        break
    elif score <= 0:
        print("任务失败！")
        break