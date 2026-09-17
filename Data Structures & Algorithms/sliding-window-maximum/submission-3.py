class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        w=[]
        ans=[]

        for i in range(k):
            heapq.heappush(w,[-nums[i],i])
        
        ans.append(-(w[0][0]))

        for i in range(k,len(nums)):
            heapq.heappush(w,[-nums[i],i])
            while w[0][1]<i-k+1:
                heapq.heappop(w)
            
            ans.append(-(w[0][0]))
        
        return ans