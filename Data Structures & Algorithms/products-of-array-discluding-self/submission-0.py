class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        
        temp=1
        for i in range(0,n):
            res[i]=temp
            temp*=nums[i]
        
        temp=1
        for i in range(n-1,-1,-1):
            res[i]*=temp
            temp*=nums[i]
        
        
        return res

