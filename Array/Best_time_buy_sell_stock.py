def maxProfit(prices):
    buy=prices[0]
    profit=0
    for i in range(1,len(prices)):
        buy=min(buy,prices[i])
        profit=max(profit,prices[i]-buy)
        
    return profit