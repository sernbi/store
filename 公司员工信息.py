import json
information = {'刘备':{'年龄':'56','性别':'男','编号':'106','任职公司':'IBM','薪资':500,'部门编号':'50'},
               '大乔':{'年龄':'19','性别':'女','编号':'230','任职公司':'微软','薪资':501,'部门编号':'60'},
               '小乔':{'年龄':'19','性别':'女','编号':'210','任职公司':'Oracle','薪资':600,'部门编号':'60'},
               '张飞':{'年龄':'45','性别':'男','编号':'230','任职公司':'Tencent','薪资':700,'部门编号':'10'}
               }
#print(json.dumps(information,indent=4))
for key,value in information.items():
    print(key,":",value)