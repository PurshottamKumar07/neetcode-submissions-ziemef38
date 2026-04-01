class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        cor={}
        for i in range(len(nums)):
            diff=target-nums[i] 
            if diff in cor.keys():
                res.append(cor[diff])
                res.append(i)
                return res
            else:
                cor[nums[i]]=i
        return -1 

        