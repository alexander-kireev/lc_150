from math import inf

def buy_sell(prices):
    max_profit = 0
    prev = inf

    for price in prices:
        if prev < price:
            max_profit += price - prev
            prev = price
        else:
            prev = min(price, prev)

    return max_profit







prices = [7,1,5,3,6,4]
#Output: 7
print(buy_sell(prices))