num = int(input())
times = 1
flag = 1
if num < 0:
    flag = 0
for i in range(1,num+1):
    flag = 1
    if num == 0:
        times = 1
        break
    else:
        times *= i
if flag == 1:
    print("{}的阶乘为{}".format(num,times))
else:
    print("输入数据不合法")