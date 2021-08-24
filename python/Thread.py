import time
from threading import Thread

bread = 0


class customer(Thread):
    name = ''
    money = 3000
    count = 0

    def setn(self, name):
        self.name = name

    def run(self) -> None:
        global bread
        while 1:
            if bread >= 1:
                bread -= 1
                self.count += 1
                self.money -= 3
                if self.money < 3:
                    print(self.name, "共买了", self.count, "个面包")
                    break
            else:
                time.sleep(2)


class chef(Thread):
    count = 0
    name = ''

    def setn(self, name):
        self.name = name

    def run(self) -> None:
        global bread
        while 1:
            if bread < 500:
                bread += 1
                self.count += 1
                time.sleep(0.01)

            else:
                print("篮中已满",self.name,"当前做了：", self.count)
                time.sleep(2)

c1 = chef()
c2 = chef()
c3 = chef()
g1 = customer()
g2 = customer()
g3 = customer()
g4 = customer()
g5 = customer()
g6 = customer()

c1.setn("厨师1")
c2.setn("厨师2")
c3.setn("厨师3")
g1.setn("张三")
g2.setn("李四")
g3.setn("王五")
g4.setn("赵六")
g5.setn("赵七")
g6.setn("赵八")

c1.start()
c2.start()
c3.start()
g1.start()
g2.start()
g3.start()
g4.start()
g5.start()
g6.start()