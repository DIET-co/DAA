class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxProfit = 0
        buyPrice = prices[0]

        for sellPrice in prices[1:]:
            profit = sellPrice - buyPrice

            if profit < 0:
                if sellPrice < buyPrice:
                    continue
                else:
                    buyPrice = sellPrice
            else:
                maxProfit = max(maxProfit, profit)

        return maxProfit

prices = [5, 7, 5, 3, 6, 4]
solution = Solution()
maxProfit = solution.maxProfit(prices)
print(maxProfit)