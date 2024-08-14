#best days to buy stocks
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    min_val = prices[0]
    max_val = prices[0]
    for num in prices:
        if num < min_val:
            min_val = num
    for num in prices:
        if num > max_val:
            max_val = num

    if prices.index(max_val) < prices.index(min_val):
        return 0   
    return (max_val-min_val) 





print(maxProfit([7,1,5,3,6,4]))