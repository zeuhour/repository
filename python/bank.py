import pymysql, time, random

zhanghu = ('用户名', '密码', '国籍', '省份', '街道', '门牌号')
db = pymysql.connect(host="localhost", user="root", password="123456", db="bank")  # 数据库连接
custor = db.cursor()

usernow = ''  # 当前用户


def login(uname, upwd):  # 登录验证
    sql = "select * from user where username=%s and userpassword =%s"
    custor.execute(sql, (uname, upwd))
    results = custor.fetchall()
    if results:
        return 1
    else:
        return 0


def createuser(newu):  # 开户
    sql = "select username from user"
    custor.execute(sql)
    re = custor.fetchall()
    if len(re) < 100 and (newu[0],) not in re:
        id = str(random.randint(10000000000, 99999999999))
        sql = "insert into user values (%s,%s,%s,%s,%s,%s,%s,0)"
        custor.execute(sql, (newu[0], newu[1], newu[2], newu[3], newu[4], newu[5], id))
        db.commit()
        print("开户成功！您的账号为：", id)
        return 1
    elif len(re) >= 100:
        return 3
    elif (newu[0],) in re:
        return 2


def userinfo():  # 用户信息
    newu = [''] * 6
    for i in range(len(zhanghu)):
        print("请输入您的", zhanghu[i], end="：")
        newu[i] = input()
    a = createuser(newu)
    if a == 1:
        print("感谢您选择本银行！")
    elif a == 2:
        print("您的用户名已被注册，请登录！")
    elif a == 3:
        print("银行用户数已满！")


def loginservice():  # 登录操作
    i = 3
    global usernow
    while i:
        uname = input("请输入用户名：")
        upwd = input("请输入密码：")
        if login(uname, upwd):
            print(uname, "，欢迎使用！")
            usernow = uname
            break
        else:
            i -= 1
            print("用户名或密码错误，您还有", i, "次机会！")
            if i == 0:
                print("密码错误次数过多，系统锁定！")
                time.sleep(1000)


def drawm():  # 取钱
    m = input("请输入金额：")
    if m <= '0':
        print("输入金额有误，请重新选择")
        return 0
    sql = "select money from user where username=%s"
    custor.execute(sql, usernow)
    res = custor.fetchone()
    if int(res[0]) >= int(m):
        print("取款成功!")
        sql = "update user set money = money-%s where username = %s"
        custor.execute(sql, (m, usernow))
        db.commit()
    else:
        print("您的余额不足！")


def savem():  # 存钱
    m = input("请存入金额：")
    if m <= '0':
        print("输入金额有误，请重新选择")
        return 0
    sql = "update user set money=money+%s where username=%s"
    custor.execute(sql, (m, usernow))
    db.commit()
    print("存款成功！")


def tranm():  # 转账
    m = input("请输入金额：")
    sql = "select money from user where username=%s"
    custor.execute(sql, usernow)
    res = custor.fetchone()
    if int(res[0]) >= int(m):
        id = input("请输入对方账号：")
        custor.execute("select * from user where id =%s", id)
        u = custor.fetchall()
        if u:
            custor.execute("update user set money = money-%s where username=%s", (m, usernow))
            db.commit()
            custor.execute("update user set money = money+%s where id=%s", (m, id))
            db.commit()
            print("转账成功！")
        else:
            print("对方账号不存在")
    else:
        print("您的余额不足")


def selm():  # 查询
    custor.execute("select money from user where username=%s", usernow)
    re = custor.fetchone()
    print("您的余额为：", re[0])


def menu():  # 主页面
    info = '''
        ****************************************
        *        中国工商银行账户管理系统V1.0       *
        ****************************************
        *  1.开户                               *
        *  2.登录                               *
        *  输入‘退出’，退出系统！                  *
        ****************************************
        -----------请您登录后进行后续操作!----------
    '''
    print(info)


def smenu():  # 交易界面
    info = '''
        ----------------------------------------
                      您好！ %s                
        ****************************************
        *  1.取钱                               *
        *  2.存钱                               *
        *  3.转账                               *
        *  4.查询余额                            *
        *  5.返回上一级                          *
        ****************************************
    '''
    print(info % usernow)


# 主程序
while 1:
    menu()
    c = input("请选择功能：")
    if c == '退出':
        print("欢迎下次使用！")
        db.close()
        exit()
    elif c == '1':
        userinfo()
        time.sleep(1)
    elif c == '2':
        loginservice()
        time.sleep(1)
    else:
        print("请输入正确内容！")
    if usernow != '':
        while 1:
            smenu()
            c = input("请选择功能：")
            if c == '1':
                drawm()
                time.sleep(1)
            elif c == '2':
                savem()
                time.sleep(1)
            elif c == '3':
                tranm()
                time.sleep(1)
            elif c == '4':
                selm()
                time.sleep(1)
            elif c == '5':
                break
            else:
                print("请输入正确内容！")
