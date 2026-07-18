class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums)==1:
            return nums[0]
        
        def rec(n,memo):
            if n>=len(nums):
                return 0

            if n in memo:
                return memo[n]
            
            else:
                memo[n]=max(rec(n+2,memo)+nums[n],
                            rec(n+3,memo)+nums[n])
                
                return memo[n]
        
        memo={}
    
        return max(rec(0,memo),rec(1,memo))