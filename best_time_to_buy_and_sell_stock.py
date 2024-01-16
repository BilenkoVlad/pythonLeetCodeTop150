class BestTimeToBuyAndSellStock:
    @staticmethod
    def max_profit(prices: list[int]) -> int:
        result = {}

        for buy in range(len(prices) - 1):
            profit = 0
            for sell in range(buy + 1, len(prices)):
                if profit < prices[sell] - prices[buy]:
                    profit = prices[sell] - prices[buy]
                    result[buy + 1] = profit

        return_value = 0
        for profit in result.values():
            if profit >= return_value:
                return_value = profit

        return return_value

# Input: prices = [7,1,5,3,6,4]
# Output: 5
