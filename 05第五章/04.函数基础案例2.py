def calc_order_cost(*args, coupon = 0, score = 0, express = 0):
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

total = calc_order_cost(("鼠标", 188, 2), ("键盘", 388, 1), ("手机", 3999, 1), coupon= 10, score= 4000, express= 9.9)
print(total)

total = calc_order_cost(("鼠标", 188, 2), ("键盘", 388, 1), ("手机", 6999, 1), coupon= 10, score= 4000, express= 9.9)
print(total)