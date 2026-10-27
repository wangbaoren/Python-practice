"""
类型注解是python中的一种语法特性,用于明确标识变量,函数参数和返回值的数据类型,从而使代码更清晰
类型推断:Python解释器自动推断出变量,表达式或函数的返回值的数据类型的能力,而无需开发者显式声明
类型注解只是起到语法提示作用,并不会影响程序运行结果
"""
a: int = 958
score: float = 98.5
hobby: str = "abc"

name2 = ["a", "b", "c", 100]
names: list[str | int] = ["a", "b"]
phones: set[str] = {"11111", "22222"}
options: dict[str, int] = {"count": 0,"total": 0}
goods: tuple[str, int, bool] = ("aaa", 789, True)

names.append(89)
name2.append(89)

"""
函数类型注解:主要就是为函数的参数和返回值添加类型注解
"""
# def calc(scores: list[int]) -> float:#返回值类型
#     return sum(scores) / len(scores)
# def calc_data(scores: list[int]) -> tuple[int, int, float]:
#     max_v = max(scores)
#     min_v = min(scores)
#     avg_v = sum(scores) / len(scores)
#     return max_v, min_v, avg_v

def calc_order(*args: tuple[str, float, int], coupon: int = 0, score: int = 0, express: int = 0) -> float:
    """
    根据输入的商品信息(商品名称,商品价格,商品数量),优惠卷,积分抵扣,运费.计算订单总价格
    :param args: 商品信息(商品名称,价格,数量),如:(("鼠标", 249, 2), ("键盘", 654, 3))
    :param coupon: 优惠卷金额
    :param score: 积分抵扣
    :param express: 运费
    :return:
    """
    #1.计算商品总价格
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)
    #2.扣减优惠券
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon
    #3.扣减积分抵扣
    if total_cost >= 5000 and score // 100 <= total_cost:
        total_cost -= score // 100
    #4.添加运费
    total_cost += express
    return total_cost

total = calc_order(("鼠标", 188, 2), ("键盘", 388, 1), ("手机", 3999, 1), coupon=10, score=4000, express=9.9)
print(total)

total = calc_order(("鼠标", 188, 2), ("键盘", 388, 1), ("手机", 6999, 1), coupon=10, score=4000, express=9.9)
print(total)