class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0
        b=0
        ans,temp=0,0
        comp=[0]*len(height)

        for i in range(len(height)-1,-1,-1):
            if height[i]>temp:
                temp=height[i]
            comp[i]=temp
        
        for i in range(len(height)):
            if height[i]>=b:
                b=height[i]
            else:
                ans+=min(b,comp[i])-height[i]
        
        return ans