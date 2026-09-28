class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        for i in range(len(prices)):
            if max(prices[i:]) - prices[i] > maxProf:
                maxProf = max(prices[i:]) - prices[i]
        return maxProf
