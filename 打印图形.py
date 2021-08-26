n= 5
for i in range(n):
    a = n - i
    b = 2 * i + 1
    for j in range(a):
        print(' ', end='')
    for k in range(b):
        print('*',end='')
    print('')