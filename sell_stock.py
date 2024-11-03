def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        else:
            profit = prices[i] - min_price
            if profit > max_profit:
                max_profit = profit

    return max_profit

profit = max_profit([7, 1, 5, 3, 6, 4])
print(profit)  
