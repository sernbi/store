import random
print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、取钱              ------------|")
print("|------------3、存钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
bank={'frank': {'account': 88474479, 'password': '1234', 'country': '1', 'province': '1', 'street': '1', 'door': '1', 'money': 1000, 'bank_name': '狼腾测试猿银行'},
      'abc': {'account':12345678, 'password': '1234', 'country': '1', 'province': '1', 'street': '1', 'door': '1', 'money': 1000, 'bank_name': '狼腾测试猿银行'},
      '456': {'account':88888888, 'password': '1234', 'country': '1', 'province': '1', 'street': '1', 'door': '1', 'money': 1000, 'bank_name': '狼腾测试猿银行'},
      'liuxing': {'account': 66666666, 'password': '1234', 'country': '1', 'province': '1', 'street': '1', 'door': '1', 'money': 1000, 'bank_name': '狼腾测试猿银行'}}#创建一个空的字典
#开户逻辑
bank_name="狼腾测试猿银行"



#                第一个对应第一个 不是名称对应名称
def bank_adduser(account,username,password,country,province,street,door):
    if  len(bank) >100:
        return 3
    if username in bank:#  如变量在容器内执行下面的代码
        return 2
    bank[username]={
        "account":account,#
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":0,
        "bank_name":bank_name
    }
    return 1
def adduser():#定义了一个方法
    username=input("请输入您的用户名")
    password = input("请输入您的密码")
    print("请输入您的地址")
    country=input("\t\t请输入您的国家")
    province=input("\t\t请输入您的省份")
    street=input("\t\t请输入您的街道")
    door=input("\t\t请输入您的门牌号")
    account=random.randint(10000000,99999999)
    stast=bank_adduser(account,username,password,country,province,street,door)
    #        调用方法   （元素，，，，，，，，，）
    if stast ==3 :
        print("你去别的银行吧")
    elif stast== 2:
        print("开户失败，你别重复")
    elif stast== 1:
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))

#存钱
def addmoney():
    account = int(input("请输入您的账号"))
    username= list(bank.keys())
    for i in range(len(username)):
        if account == bank[username[i]]['account']:
            money = bank[username[i]]['money']
            print("欢迎")
            print("您的余额：", money)
            money1 = int(input("请输入想要储蓄的金额："))
            money = money + money1
            bank[username[i]]['money'] = money
            info = '''
                        ------------个人信息------------
                        用户名:%s
                        账号：%s
                        余额：%s
                        开户行名称：%s
                    '''
            # 每个元素都可传入%
            print(info % (username[i], account, money, bank_name))
        else:
            return 0
    return 1
#{'frank': {'y': 88474479, 'password': '1234', 'country': '1', 'province': '1', 'street': '1', 'door': '1', 'money': 0, 'bank_name': '狼腾测试猿银行'}}

#取钱
def remoney():
    account= int(input("请输入您的账号："))
    password = input("请输入您的密码：")
    username= list(bank.keys())
    for i in range(len(username)):
        if account == bank[username[i]]['account']:
            if password == bank[username[i]]['password']:
                money = bank[username[i]]['money']
                print("欢迎")
                print("您的余额：", money)
                money1 = int(input("请输入想要取出的金额："))
                if money1 <= money:
                    money = money - money1
                    bank[username[i]]['money'] = money
                    info = '''
                                ------------个人信息------------
                                用户名:%s
                                账号：%s
                                余额：%s
                                开户行名称：%s
                            '''
                    # 每个元素都可传入%
                    print(info % (username[i], account,money, bank_name))
                else:
                    print(("余额不足"))
            else:
                print("密码错误")
        else :
            print("账号不存在")
    return 1

# begin=input("请选择业务")
while True:
    begin = input("请选择业务")
    if begin =="1":#您输入的业务等于1执行开户操作
        adduser()
    elif begin == "2":
        print(2, "、存钱")
        addmoney()
    elif begin == "3":
        print(3,"、取钱")
        remoney()
    elif begin == "4":
        print(4,"、转账")
    elif begin == "5":
        print(5,"、查询")
    else:
        print(6,"、退出")
        break

money = 0
if begin == 2:
    print("欢迎")
    print("您的余额：",money)
    money1 = int(input("请输入想要储蓄的金额："))
    money = money +money1
    bank['money'] = money




