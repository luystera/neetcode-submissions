class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        prev_min = prices[0]
        # dp[i] is the profit if you sell at index i given the prev_min
        for i in range(1,len(prices)):
            dp[i] = prices[i] - prev_min
            if (prev_min > prices[i]):
                prev_min = prices[i]
        return max(dp)