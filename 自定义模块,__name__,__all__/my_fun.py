# __all__是一个模块级别的特殊变量,用于指定from 模块名 import * 回导入哪些功能(*通配了哪些功能)
# __all__控制的是 from...import * 时,要导入的功能,并不会影响直接导入具体的功能(如from...import 功能)
__all__ = ["log_separator1", "log_separator2", "log_separator3"]

#常量(不会发生变化的数据,常量的名称为全部大写)
PI = 3.14
NAME = "xxxx"
def log_separator1():
    print("-" * 30)#"-"重复输出30次

def log_separator2():
    print("+" * 30)

def log_separator3():
    print("#" * 30)

def log_separator4():
    print("*" * 30)

# 测试函数
# __name__: Python中内置变量,表示当前模块的名字(直接运行当前模块,__name__的值为__main__;当模块被导入时,__name__的值为模块的名字)
if __name__ == "__main__":
    log_separator1()