class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        ans=0
        st=[]

        for i,h in enumerate(heights):
            start=i
            while st and st[-1][1]>h:
                ind,v=st.pop()
                ans=max(ans,(i-ind)*v)
                start=ind
            st.append([start,h])
        
        while st:
            ind,v=st.pop()
            ans=max(ans,(len(heights)-ind)*v)
        
        return ans