class Solution:
    def climbStairs(self, n: int) -> int: 
        def dp(n,memo):
            if n in memo:
                return memo[n]
            else:
                memo[n]=dp(n-1,memo)+dp(n-2,memo)
                return memo[n]
        
        memo={0:1,1:1}
        return dp(n,memo)