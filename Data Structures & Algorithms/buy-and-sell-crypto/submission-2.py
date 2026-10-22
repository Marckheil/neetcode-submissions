class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0          # buy day: cheapest price seen so far
        profit = 0
        for right in range(len(prices)):   # sell day
            if prices[right] < prices[left]:
                left = right               # found a cheaper buy day, move there
            else:
                profit = max(profit, prices[right] - prices[left])
        return profit