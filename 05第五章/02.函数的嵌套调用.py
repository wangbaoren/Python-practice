#函数调用遵循栈结构,最后调用的函数最先返回LIFO(Last In First Out)后进先出

#函数嵌套调用
def function_a():
    print("a...before")
    function_b()
    print("a...after")

def function_b():
    print("b...before")
    function_c()
    print("b...after")

def function_c():
    print("c...")

function_a()