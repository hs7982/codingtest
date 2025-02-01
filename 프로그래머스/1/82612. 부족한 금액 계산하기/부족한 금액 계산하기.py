def solution(price, money, count):
    price_calc = 0
    for i in range(count+1):
        price_calc += price * i
    if price_calc - money < 0:
        return 0
    else:
        return price_calc - money

