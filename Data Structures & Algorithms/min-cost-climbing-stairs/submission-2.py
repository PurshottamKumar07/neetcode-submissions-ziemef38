class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def rec(n,memo):
            if n>=len(cost):
                return 0
            if n in memo:
                return memo[n]
            else:
                memo[n]=min(rec(n+1,memo)+cost[n],rec(n+2,memo)+cost[n])
                return memo[n]

        memo={}  

        return min(rec(0,memo),rec(1,memo))