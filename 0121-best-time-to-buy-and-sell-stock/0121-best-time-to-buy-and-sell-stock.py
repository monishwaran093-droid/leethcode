class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprices=prices[0]
        maxprofit=0
        for i in range(1,len(prices)):
                minprices=min(minprices,prices[i])
                maxprofit=max(maxprofit,prices[i]-minprices)
        return maxprofit