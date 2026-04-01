class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans=0
        lm=0
        for i in range(1,len(prices)):
            if prices[lm]>prices[i]:
                lm=i
            else:
                ans=max(ans,prices[i]-prices[lm])
        return ans