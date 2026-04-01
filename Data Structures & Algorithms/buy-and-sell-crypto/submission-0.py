class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l=len(prices)
        ans=0
        for i in range(l):
            for j in range(i,l):
                if prices[j]>prices[i]:
                    ans=max(ans,prices[j]-prices[i])
        
        return ans