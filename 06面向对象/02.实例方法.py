"""
在类中定义实例方法时,定义语法和函数定义的方式一致
定义实例方法:
# 定义类
class 类名:
    def __init__(self, 形参列表):
        self.属性名 = 参数值
        self.属性名 = 参数值

    def 方法名(self, 形参列表):
        ...
    def 方法名(self, 形参列表):
        ...

#创建对象
对象名 = 类名(参数列表)
对象名.方法名(实参)
"""

class Car:
    def __init__(self, brand, name, price):
        self.brand = brand
        self.name = name
        self.price = price
    def running(self):
        print(f"{self.brand},{self.name}正在高速运行...")
    def total_cost(self, discount: float, rate: float) -> float:
        """
        计算提车的总费用, 包含两个部分:车的价格,税费
        :param discount: 折扣
        :param rate: 税率
        :return: 提车的总费用
        """
        return self.price * discount + self.price * rate
c1 = Car("BMW", "X5", 500000)
c1.running()
total_price = c1.total_cost(0.9, 0.1)
print(f"提车的总价为{total_price: .0f}")