# 可以通过type()语句来得到数据的类型,具体语法为:type(要查看的数据类型)
# 变量本身是没有类型的,type(变量)输出的类型是变量中存储的数据的类型
print(type("Hello World"))#str
print(type(10))#int
print(type(3.14))#float
print(type(True))#bool
print(type(False))#bool
print(type(None))#NoneType
print("----------------------------------------------")

# 也可通过isinstance()检查数据是否属于指定的类型,返回的是一个bool值,具体语法是:isinstance(数据,数据类型)
print(isinstance("Hello World", bool))
print(isinstance("Hello World", str))