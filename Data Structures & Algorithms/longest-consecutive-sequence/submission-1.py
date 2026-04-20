class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=set(nums)
        temp=1
        ans=0
        
        for i in range(len(nums)):
            temp2=nums[i]+1
            while temp2 in num:
                temp+=1
                temp2+=1
            ans=max(temp,ans)
            temp=1
        
        return ans
            