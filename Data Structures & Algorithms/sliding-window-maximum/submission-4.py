class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        dq=deque()
        ans=[]

        for i in range(k):
            while dq and nums[i]>dq[-1][0]:
                dq.pop()
            dq.append([nums[i],i])

        ans.append(dq[0][0])

        for i in range(k,len(nums)):
            while dq and dq[0][1] < i - k + 1:
                dq.popleft()

            while dq and nums[i] > dq[-1][0]:
                dq.pop()
            dq.append([nums[i],i])
            ans.append(dq[0][0])
        
        return ans