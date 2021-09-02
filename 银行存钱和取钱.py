import random
print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、存钱              ------------|")
print("|------------3、取钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
bank={12345678: {'username': 'frank', 'password': '1234', 'country': '1', 'province': '1', 'street': '1', 'door': '1', 'money': 1000, 'bank_name': '狼腾测试猿银行'},
      66666666: {'username':'123', 'password': '1234', 'country': '1', 'province': '1', 'street': '1', 'door': '1', 'money': 1000, 'bank_name': '狼腾测试猿银行'},
      88888888: {'username':'456', 'password': '1234', 'country': '1', 'province': '1', 'street': '1', 'door': '1', 'money': 1000, 'bank_name': '狼腾测试猿银行'},
      99999999: {'username':'789', 'password': '1234', 'country': '1', 'province': '1', 'street': '1', 'door': '1', 'money': 1000, 'bank_name': '狼腾测试猿银行'}}#创建一个空的字典
#开户逻辑
bank_name="狼腾测试猿银行"



#                第一个对应第一个 不是名称对应名称
def bank_adduser(account,username,password,country,province,street,door):
    if  len(bank) >100:
        return 3
    if username in bank:#  如变量在容器内执行下面的代码
        return 2
    bank[account]={
        "username":username,#
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
        print(info % (username, account, country, province, street, door, bank[account]["money"], bank_name))

#{'frank': {'y': 88474479, 'password': '1234', 'country': '1', 'province': '1', 'street': '1', 'door': '1', 'money': 0, 'bank_name': '狼腾测试猿银行'}}


#存钱
def addmoney():
    account = int(input("请输入您的账号"))
    # account ="account" in bank
    if account in bank.keys():
        money1 = int(input("请输入您需要存入的金额："))
        money = bank[account]['money']
        money = money + money1
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (bank[account]['username'], account, money, bank_name))

        print("您现在的余额为：",money)
    else:
        print("您的账户输入错误")
#取钱
def remoney():
    account= int(input("请输入您的账号："))
    password = input("请输入您的密码：")
    # username= list(bank.keys())
    # for i in range(len(username)):
    if account in bank.keys():
        if password == bank[account]['password']:
            money = bank[account]['money']
            print("欢迎")
            print("您的余额：", money)
            money1 = int(input("请输入想要取出的金额："))
            if money1 <= money:
                money = money - money1
                bank[account]['money'] = money
                info = '''
                            ------------个人信息------------
                            用户名:%s
                            账号：%s
                            余额：%s
                            开户行名称：%s
                        '''
                # 每个元素都可传入%
                print(info % (bank[account]['username'], account,money, bank_name))
            else:
                print(("余额不足"))
        else:
            print("密码错误")
    else :
        print("账号不存在")
    return 1


#转账
def zhuanzhang():
    account1 = int(input("请输入转出的账号："))
    account2 = int(input("请输入转入的账号："))
    if account1 in bank.keys() and account2 in  bank.keys():
        password1 = str(input("请输入转出账号的密码："))
        password2 = str(input("请输入转入账号的密码："))
        if password1 in  bank[account1]["password"] and password2 in bank[account2]["password"]:
            mvmoney = int(input("请输入您要转出的金额："))
            if mvmoney < bank[account1]["money"]:
                money = bank[account1]["money"] - mvmoney
                bank[account1]["money"] = money
                getmoney = bank[account2]["money"] + mvmoney
                bank[account2]["money"] = getmoney
                print("转出",mvmoney,"元后，您的账号",account1,"余额为：",money)
                print("转入账号",account2,"的余额为：",getmoney)
            else:
                print("您的余额不足")
        else:
            print("密码错误")
    else:
        print("用户不存在")

#查询
def chaxun():
    account = int(input("请输入您的账号："))
    if account in bank.keys():
        password = input("请输入密码：")
        if password == bank[account]['password']:
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
            print(info % (bank[account]['username'], account, bank[account]['country'], bank[account]['province'], bank[account]['street'], bank[account]['door'], bank[account]["money"], bank[account]['bank_name']))
    else:
        print("用户不存在")


#begin=input("请选择业务")
while True:
    begin = input("请选择业务：")
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
        zhuanzhang()
    elif begin == "5":
        print(5,"、查询")
        chaxun()
    else:
        print(6,"、退出")
        break





