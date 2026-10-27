"""
在Python中,所有类默认继承object类,object类是顶级类或基类,其他子类叫做派生类
继承:一个类从另一个已有的类获得其成员的相关特性,叫做继承(站在子类角度)
派生:从一个已有的类产生一个新的类,称为派生(站在父类角度)
继承和派生就是从不同方向描述的相同概念
父类:也叫基类,指以已有被继承的类
子类:也叫派生类或扩展类
继承形式:
class 父类名(object):
    ...
class 子类(父类):
    ...

当子类继承父类时,子类拥有和父类完全一样的功能,但却不用再写大量重复代码.
继承的作用:提高代码的复用率.减少重复代码的书写
"""
# 父类
class Father(object):
    def __init__(self):
        self.sex = "男"
    def walk(self):
        print("喜欢散步行走... ")
    def __str__(self):
        return f"{self.sex}"


class Son(Father):
    pass

Father = Father()
print(Father)
son = Son()
print(son)

"""
单继承指一个子类只能继承自一个父类,不能继承多个类.这个子类会具有父类的属性和方法
基本语法:
# 父类Father
class Father(object):
    pass
# 子类Son
class Son(Father):
    pass
    
多继承:一个类同时继承了多个父类,并且同时具有所有父类的属性和方法
基本语法:
# 父类1 Father
class Father(object):
    pass
# 父类2 Mother
class Mother(object):
    pass
# 子类 Son
class Son(Father, Mother):
    pass
"""
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'
    def make(self):
        print(f"运用{self.kongfu}制作煎饼果子")
class School(object):
    def __init__(self):
        self.kongfu = '[学校AI煎饼果子配方]'
    def make(self):
        print(f"运用{self.kongfu}制作煎饼果子")

class Son(Master, School):
    pass

son = Son()
print(son.kongfu)
son.make()

"""
当一个类有多个父类时，默认使用第一个父类的同名属性和方法，可以使用 类名.__mro__属性 或 类名.mro()方法查看调用的先后顺序
注:MRO(Method Resolution Order): 方法解析顺序
#通过属性查看引用顺序
print(类名.__mro__)
#通过方法查看引用顺序
print(类名.mro())
"""

print(Son.__mro__)
print(Son.mro())