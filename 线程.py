from threading import Thread
import time
lanzi = 0
money = 3000
class cook(Thread):
    def run(self) -> None:
        global lanzi
        global money
        while True:
            if lanzi >= 0 and lanzi < 500:
                lanzi = lanzi + 1
                print("做了一个蛋挞")
            elif lanzi == 500:
                print("篮子已满")
                time.sleep(3)

class shop(Thread):
    #money = 3000
    def run(self) -> None:
        global lanzi
        global money
        while True:
            if lanzi > 0 and money > 0:
                lanzi = lanzi - 1
                money = money - 2
                print("您花2块钱买了一个蛋挞")
            elif lanzi == 0:
                print("篮子已空")
                time.sleep(2)
            elif money == 0:
                break
            print(money)

c1 = cook()
c2 = cook()
c3 = cook()
s1 = shop()
s2 = shop()
s3 = shop()
s4 = shop()
s5 = shop()
s6 = shop()

c1.start()
c2.start()
c3.start()
s1.start()
s2.start()
s3.start()
s4.start()
s5.start()
s6.start()
