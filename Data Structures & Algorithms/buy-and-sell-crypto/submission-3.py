class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # - start at i 
        # - check profit for each one against i by subtracting 
        # - record max profit from all iterations of i 


        # left pointer 
        # right pointer 

        # while loop through prices 
        #     profit = right val - left val 
        #     if profit < 0
        #         r + 1
        #         continue 
        #     elif profit > 0 
        #         maximum = max(maximum, profit)
                #r+1

            l, r = 0, 1
            maximum = 0 
            while r < len(prices):
                profit = prices[r] - prices[l]
                if profit < 0:
                    l = r
                else: 
                    maximum = max(maximum, profit)
                r += 1
            return maximum 
                