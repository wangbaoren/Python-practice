"""
属性分为:
    实例属性:实例属性属于每个具体对象的属性,每个对象都是独立的.(各个对象持有的数据)
    类属性:类属性是属于类本身的属性,所有实例共享的.(所有对象共享的数据或配置)
    因为类属性是所有实例对象共享的,因此类属性也可以通过实例对象.属性的方式操作
        但通过实例查找属性时,会先查找实例属性,实例属性不存在时,再查找类属性
"""
class Car:
    # 类属性 ---> 通过 类名.属性 的方式操作
    wheel = 4 # 轮胎数量
    tax_rate = 0.5 # 购置税
    def __init__(self, brand, name, price):
        # 实例属性 ---> 通过 实例对象.属性 的方式操作
        self.brand = brand
        self.name = name
        self.price = price
        self.wheel = 2
    def running(self):
        print(f"{self.brand},{self.name}正在高速运行...")
    def __str__(self):
        return f"{self.price}"
c1 = Car("BMW", "X5", 500000)
print(c1)
c1.price = 10000
print(c1)
print(Car.wheel)
Car.wheel = 80
print(Car.wheel)
print(c1.wheel)