import xlrd
#工作簿
wb = xlrd.open_workbook(filename = r"F:\python自动化\day07【mysql工具类与excel读取】\2020年每个月的销售情况.xlsx")
#确定选项卡
sh = wb.sheet_names()
sh1 = len(sh)
#全年销售总额
sum = 0
sum1 = 0
yurongfu = 0
niuzaiku = 0
fengyi = 0
picao = 0
Tshirt = 0
majia = 0
yrfj = 0
nzkj = 0
fyj = 0
pcj = 0
tsj = 0
mjj = 0
for i in range(sh1):
    read = sh[i]
    sum2 = 0
    yrf = 0
    nzk = 0
    fy = 0
    pc = 0
    ts = 0
    mj = 0
    sheet = wb.sheet_by_index(i)
    for j in range(1, sheet.nrows):
        data = sheet.row_values(j)
        a = data[2] * data[4]
        sum1 = sum1 + data[4]
        sum2 = sum2 +a
        sum = sum + a
        if data[1] == "羽绒服":
            b = data[2] * data[4]
            yrfj = yrfj + data[4]
            yurongfu = yurongfu + b
            yrf = yrf + b
            yb1 = yrf / sum2
            yb = yurongfu / sum
            yjb = yrfj / sum1
        elif data[1] == "牛仔裤":
            c = data[2] * data[4]
            nzkj = nzkj + data[4]
            niuzaiku = yurongfu + c
            nzk = nzk + c
            nb1 = nzk / sum2
            nb = niuzaiku / sum
            njb = nzkj / sum1
        elif data[1] == "风衣":
            d = data[2] * data[4]
            fyj = fyj + data[4]
            fengyi = fengyi + d
            fy = fy + d
            fb1 = fy / sum2
            fb = fengyi / sum
            fjb = fyj / sum1
        elif data[1] == "皮草":
            e = data[2] * data[4]
            pcj = pcj + data[4]
            picao = picao + e
            pc = pc + e
            pb1 = pc / sum2
            pb = fengyi / sum
            pjb = pcj / sum1
        elif data[1] == "T血":
            f = data[2] * data[4]
            tsj = tsj +data[4]
            Tshirt = Tshirt + f
            ts = ts + f
            tb1 = ts / sum2
            tb = Tshirt / sum
            tjb = tsj / sum1
        elif data[1] == "马甲":
            g = data[2] * data[4]
            mjj = mjj +data[4]
            majia = majia + g
            mj = mj + g
            mb1 = mj / sum2
            mb = majia / sum
            mjb = mjj / sum1
    print(i+1, "月羽绒服的月销售额占比：%.2f%%" % (yb1 * 100))
    print(i+1, "月牛仔裤的月销售额占比：%.2f%%" % (nb1 * 100))
    print(i+1, "月风衣的月销售额占比：%.2f%%" % (fb1 * 100))
    print(i+1, "月皮草的月销售额占比：%.2f%%" % (pb1 * 100))
    print(i+1, "月T恤的月销售额占比：%.2f%%" % (tb1 * 100))
    print(i+1, "月马甲的月销售额占比：%.2f%%" % (mb1 * 100))

print(sum)
print("羽绒服的销售额占比：%.2f%%"%(yb*100))
print("牛仔裤的销售额占比：%.2f%%"%(nb*100))
print("风衣的销售额占比：%.2f%%"%(fb*100))
print("皮草的销售额占比：%.2f%%"%(pb*100))
print("Txu的销售额占比：%.2f%%"%(tb*100))
print("马甲的销售额占比：%.2f%%"%(mb*100))
print("羽绒服的件数占比：%.2f%%"%(yjb*100))
print("牛仔裤的件数占比：%.2f%%"%(njb*100))
print("风衣的件数占比：%.2f%%"%(fjb*100))
print("皮草的件数占比：%.2f%%"%(pjb*100))
print("T恤的件数占比：%.2f%%"%(tjb*100))
print("马甲的件数占比：%.2f%%"%(mjb*100))
cx = max(yrfj,nzkj,fyj,pcj,tsj,mjj)
if cx == yrfj:
    print("最畅销的衣服是羽绒服")
elif cx == nzkj:
    print("最畅销的衣服是牛仔裤")
elif cx == fyj:
    print("最畅销的衣服是风衣")
elif cx == pcj:
    print("最畅销的衣服是皮草")
elif cx == tsj:
    print("最畅销的衣服是T恤")
elif cx == mjj:
    print("最畅销的衣服是马甲")

xl = min(yurongfu,niuzaiku,fengyi,picao,Tshirt,majia)
if xl == yurongfu:
    print("全年销量最低的衣服是羽绒服")
elif xl == niuzaiku:
    print("全年销量最低的衣服是牛仔裤")
elif xl == fengyi:
    print("全年销量最低的衣服是风衣")
elif xl == picao:
    print("全年销量最低的衣服是皮草")
elif xl == Tshirt:
    print("全年销量最低的衣服是T恤")
elif xl == majia:
    print("全年销量最低的衣服是马甲")











