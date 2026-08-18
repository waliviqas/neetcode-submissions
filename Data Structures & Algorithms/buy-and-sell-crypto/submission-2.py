class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest_price = prices[0]
        res = 0

        for price in prices:
            if price < lowest_price:
                lowest_price = price
            else:
                profit = price - lowest_price
                res = max(res, profit)
        return res

        # [10,1,5,6,7,1]
        
        # 10 < 10 x
        # profit = 10 - 10 = 0
        # res = max(0, 0)

        # 1 < 10
        # lowest_price = 1

        # 5 < 1 x
        # profit = 5 - 1
        # res = max(0, 4) = 4

        # 6 < 1 x
        # profit = 6 - 1 = 5
        # res = max(4,5) = 5

        # 7 < 1 x
        # profit = 7 - 1 = 6
        # res = max(5, 6) = 6