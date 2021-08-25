import random
num=random.randint(1,100)
money = 100
while money:
    a = input("输入：")
    a = int(a)
    money=money-10
    if a == num :
        print("OK")
        break
    elif a < num:
        print("小于")
    else:
       print("大于")