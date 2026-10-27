"""
子类重写父类同名方法和属性
重写也叫作覆盖, 就是当子类属性或方法与父类的属性或方法名字相同时,从父类继承下来的成员可以重新定义.
子类重写父类的属性和方法,优先会调用子类的属性和方法
"""
# 1.师傅类,属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'
    def make(self):
        print(f"运用{self.kongfu}制作煎饼果子")
# 为验证多继承,添加school父类
class School(object):
    def __init__(self):
        self.kongfu = '[学校AI煎饼果子配方]'
    def make(self):
        print(f"运用{self.kongfu}制作煎饼果子")
# 2.定义徒弟类,继承师傅类和学校类,添加和父类相同的属性名和方法
class Prentice(Master, School):
    def __init__(self):
        self.kongfu = '[独创的煎饼果子技术]'
    def make(self):
        print(f"运用{self.kongfu}制作煎饼果子")

# 3.测试用徒弟类创建对象,调用实例属性和方法
if __name__ == "__main__":
    print(Prentice.__mro__)
    print(Prentice.mro())
    xiaoming = Prentice()
    print(xiaoming.kongfu)
    xiaoming.make()
