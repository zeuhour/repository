class Person:
    name = ''
    sex = ''
    age = ''
    phonename = ''
    phonebrand = ''
    phonescreem = ''
    huafei = 0.0
    utime = 0
    sc = 0

    def __init__(self, n, s, a, pn, pb, ps, h, t, sc):
        self.name = n
        self.sex = s
        self.age = a
        self.phonename = pn
        self.phonebrand = pb
        self.phonescreem = ps
        self.huafei = h
        self.utime = t
        self.sc = sc

    def pMassage(self, m):
        print("发短信")

    def Call(self, num=0, time=1):
        if num == 0:
            print("号码为空")
        elif self.huafei < 1:
            print("话费不足")
        else:
            if 0 < time <= 10:
                self.huafei -= time * 1
                self.sc += 15 * time
                print("扣除话费：", time * 1, "元")
            elif 10 < time <= 20:
                t = time - 10
                m = 10 * 1
                self.sc += 15 * 10
                m += t * 0.8
                self.sc += t * 39
                self.huafei -= m
                print("扣除话费：", m, "元")
            else:
                t = time - 20
                m = 10 * 1 + 10 * 0.8
                self.sc += 15 * 10 + 39 * 10
                m += t * 0.65
                self.sc += t * 48
                self.huafei -= m
                print("扣除话费：", m, "元")
