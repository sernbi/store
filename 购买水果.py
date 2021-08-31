info = {'苹果':32.8,'香蕉':22,'葡萄':15.5}
print(info)

Friuts = {'苹果':12.3,'草莓':4.5,'香蕉':6.3,'葡萄':5.8,'橘子':6.4,'樱桃':15.8}
info = {'小明':{'fruits':{'苹果':4,'草莓':13,'香蕉':10},'money':0},'小刚':{'fruits':{'葡萄':19,'橘子':12,'樱桃':30},'money':0}}
sum1 = info['小明']['fruits']['苹果']*Friuts['苹果']+info['小明']['fruits']['草莓']*Friuts['草莓']+info['小明']['fruits']['香蕉']*Friuts['香蕉']
sum2 = info['小刚']['fruits']['葡萄']*Friuts['葡萄']+info['小刚']['fruits']['橘子']*Friuts['橘子']+info['小刚']['fruits']['樱桃']*Friuts['樱桃']
info['小明']['money'] = sum1
info['小刚']['money'] = sum2
print(info)


#通过水果名称查询水果单价
print("--------------shop-------------------")
while True :
    name = input("输入水果名称或直接回车键退出:")
    if name=='苹果':
        print(name,'￥',Friuts[name])
    elif name=='香蕉':
        print(name,'￥',Friuts[name])
    elif name=='葡萄':
        print(name,'￥',Friuts[name])
    elif  name=='' :
        print("--------感谢使用！购物愉快！-----------")
        break
    else:
        print("没有该水果!请重新输入或者按回车键退出。")

info = {
    '小明':{
        'fruits':{'苹果':4 ,'草莓':13,'香蕉':10},
        'money':0
    } ,
    '小刚':{
        'fruits':{'葡萄':19,'橘子':12,'樱桃':30},
        'money' : 0
    }
}
Friuts_key   = list(Friuts.keys())
Friuts_value = list(Friuts.values())
info_name   = list(info.keys())  #获取购买者小明、小刚,保存到列表info_name中备用
#print(info_name)
for i in range(len(info_name)) :     #读取购买者列表长度，一个一个买家的取出使用
    info_ftuits = list(info[info_name[i]]['fruits'].keys())    #获取购买的水果种类，保存到列表info_fruits中备用
    #print(info_ftuits)
    for x in range(len(info_ftuits)) :          #读取买家所买的水果列表长度，保证不遗漏每一种水果
        for j in range(len(Friuts_key)) :       #读取商店的水果列表长度，用于与客户的水果列表对比
            if info_ftuits[x]==Friuts_key[j] :  #客户水果购物车中水果与店家所售水果对比，有：获取水果单价与数量，计算所需金额
               #先将str类型转为float以便计算，将计算得到的金额赋值给购物清单中的money
                info[info_name[i]]['money']=float(info[info_name[i]]['money'])
                info[info_name[i]]['money']=info[info_name[i]]['money']+\
                                         float(info[info_name[i]]['fruits'][info_ftuits[x]])*float(Friuts_value[j])

    #print(info[info_name[i]]['money'])

print(info['小明'])
print(info['小刚'])
print(info)