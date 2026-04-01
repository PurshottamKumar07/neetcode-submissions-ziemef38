class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans=0
        l,r=0,len(heights)-1
        while l<r:
            h=min(heights[r],heights[l])
            ans=max(ans,h*(r-l))
                
            if heights[l]<heights[r]:
                ans=max(ans,h*(r-l))
                l+=1
            else:
                r-=1
        return ans