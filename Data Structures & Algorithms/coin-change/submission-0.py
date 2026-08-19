class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp=[float('inf')]*(amount+1)

        dp[amount]=0

        for i in range(amount-1,-1,-1):
            for coin in coins:
                if coin+i<=amount:
                    dp[i]=min(dp[i],1+dp[i+coin])
        
        return -1 if dp[0]==float('inf') else dp[0]