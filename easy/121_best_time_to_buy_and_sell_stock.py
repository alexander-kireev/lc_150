def maxProfit(prices):
    if not prices:
        return
    
    min_price = prices[0]
    dif = 0

    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        else:
            if prices[i] - min_price > dif:
                dif = prices[i] - min_price
        
    return dif







prices = [7,6,4,3,1]


print(maxProfit(prices))