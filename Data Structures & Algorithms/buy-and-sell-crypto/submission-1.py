class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # keep track of the cheapest price we've seen so far (first day)
        # keep track of the max profit we've seen so far (0)
        # iterate through the numbers
        max_profit = 0
        min_price = prices[0]

        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        
        return max_profit