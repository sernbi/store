a = int(input())
b = int(input())
c = int(input())
if a == b ==c :
    print("等边三角形")
elif a+b < c or a-b > c:
    print("不能形成三角形")
elif a == b or a == c or b == c:
    print("等腰三角形")
elif a*a+b*b == c*c or a*a+c*c == b*b or b*b+c*c == a*a:
    print("直角三角形")
else:
    print("普通三角形")