mi = 3
while mi:
    name = input()
    password = input()
    mi = mi - 1
    if name == 'root' and password == 'admin':
        break
    elif mi==0:
        print("系统锁定")