import random
def shuzi(a):
    sz = {}
    for i in a:
        if i not in sz:
            sz[i] = 1;
        else:
            sz[i] += 1
    return sz
sh = []
for y in range(20):
    sh.append(random.randint(1,5))
# sh = [21,21,21,56,56,56,56,56,56,56,56,56,10,10,10]
print(sh)
x = shuzi(sh)
print(x)
