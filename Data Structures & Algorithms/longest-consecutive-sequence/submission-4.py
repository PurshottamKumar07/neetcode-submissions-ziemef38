class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            
        ver=set(nums)
        temp,ans=0,0
        for i in range(len(nums)):
            if nums[i]-1 in ver:
                continue
            s=nums[i]
            while s in ver:
                temp+=1
                s+=1
                ans=max(ans,temp)
            else:
                temp=0
        
        return ans