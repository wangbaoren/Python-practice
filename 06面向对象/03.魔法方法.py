"""
魔法方法指Python中提供的以双下划线开头和结尾的特殊方法,用于定义类的特殊行为,比如__init__
魔法方法是由Python解释器在合适时机自动调用
__init__                初始化方法
__str__                 字符串表示的方法
__eq__                  比较两个对象是否相等(equal)
支持比较两个对象的大小(小于(less than), 小于等于(less than or equal), 大于(greater than), 大于等于(greater than or equal))
__lt__                  小于(less than)
__le__                  小于等于(less than or equal)
__gt__                  大于(greater)
__ge__                  大于等于(greater than or equal)
"""

class Car:
    def __init__(self, brand, name, price):
        self.brand = brand
        self.name = name
        self.price = price
        print("Car类型的对象初始化完毕,对象属性已添加")
    def running(self):
        print(f"{self.brand} {self.name}正在高速行驶...")
    def __str__(self):
        return f"{self.brand, self.name, self.price}"
    def __eq__(self, other: object):
        if not isinstance(other, Car):
            return False
        return self.brand == other.brand and self.name == other.name and self.price == other.price
    def __lt__(self, other):
        return self.price < other.price
    def __del__(self):
        print(f"{self}对象被销毁")

c1 = Car("BMW", "X5", 50000)
print(c1)
del c1
c2 = Car("BMW", "X5", 50000)
print(c2)
c1 = Car("BMW", "X5", 50000)
print(c1 == c2)
print(c1 < c2)