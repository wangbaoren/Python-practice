"""
导入模块的具体语法:
1.
导入形式:   import 模块名
#样例:     import random, os
调用方式:   模块名.功能名
#样例:     random.randint(10,100)
2.
导入形式:   import 模块名 as 别名
#样例:     import random as rd
调用方式:   别名.功能名
#样例:     as.randint(10,100)
3.
导入形式:   from 模块名 import 功能名
#样例:     from random import randint, choice
调用方式:   功能名
#样例:     randint(10,100)
4.
导入形式:   from 模块名 import 功能名 as 别名
#样例:     from random import randint as rin
调用方式:   别名
#样例:     rin(10,100)
5.调用模块中的所有功能
导入形式:   from 模块名 import *
#样例:     from random import *
调用方式:   功能名
#样例:     randint(10,100)
"""
# import random
# import random as rd
# from random import randint
# from random import randint as rnd
from random import *
for i in range(100):
    # print(random.randint(1, 100))
    # print(rd. randint(1,100))
    # print(randint(1,100))
    # print(rnd(1,100))
    print(randint(1,100))
