class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l,r = 0, 1

        while r < len(prices):
            profit = prices[r] - prices[l]
            max_profit = max(profit, max_profit)
            if prices[l] < prices[r]:
                r += 1
            else:
                l = r
                r += 1
        
        return max_profit



        # profit = 0
        # min_price = prices[0]

        # for price in prices:
        #     profit = max(profit, price-min_price)
        #     min_price = min(price, min_price)
        
        # return profit
        

        
        # max_profit = 0
        # low = prices[0]

        # for price in prices[1:]:
        #     diff = price - low
        #     max_profit = max(diff, max_profit)
        #     low = min(price, low)
        
        # return max_profit
        
        # max_profit = 0
        # low = prices[0]

        # for price in prices[1:]:
        #     if price < low:
        #         low = price
        #     else:
        #         if price - low > max_profit:
        #             max_profit = price - low
        
        # return max_profit


    # it works , but o(n^2) can't pass the test
        # max_profit = 0
        # for i in range(len(prices)):
        #     profit = max(prices[i:]) - prices[i]
        #     if profit > max_profit:
        #         max_profit = profit
        
        # return max_profit