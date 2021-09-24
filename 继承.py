import unittest
class cook:
    __name = ""
    __age = 0

    def setname(self,setname):
        self.__name = setname
    def getname(self):
        return self.__name
    def setage(self,setage):
        if setage <= 0:
            print("输入年龄不合法")
        else:
            self.__age = setage
    def getage(self):
        return self.__age

    def zhengfan(self):
        pass
class cook1(cook):
    def chaocai(self, caiming):
        pass

class cook2(cook1):
    def zhengfan(self):
        print(self.getname(), "正在蒸饭！")
    def chaocai(self, caiming):
        print(self.getname(), "正在炒", caiming)

class cook3(unittest.main):
    pass


c = cook2()
c.setname("云中")
c.setage(25)
print(c.getname())
print(c.getage())
c.zhengfan()
c.chaocai("里脊肉")