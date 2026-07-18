class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums)==1:
            return nums[0]
        
        def intermediate(lis):
            memo={}
            return max(rec(0,lis,memo),rec(1,lis,memo))

        def rec(n,lis,memo):
            if n>=len(lis):
                return 0

            if n in memo:
                return memo[n]
            
            else:
                memo[n]=max(rec(n+2,lis,memo)+lis[n],
                            rec(n+3,lis,memo)+lis[n])
                
                return memo[n]
        
    
        return max(intermediate(nums[1:]),intermediate(nums[:-1]))