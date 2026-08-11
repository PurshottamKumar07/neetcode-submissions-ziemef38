class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        ans=0
        st=[]
        st.append([0,heights[0]])

        for i in range(1,len(heights)):
            start=i
            while st and st[-1][1]>heights[i]:
                ind,v=st.pop()
                ans=max(ans,(i-ind)*v)
                start=ind
            st.append([start,heights[i]])
        
        while st:
            ind,v=st.pop()
            ans=max(ans,(len(heights)-ind)*v)
        
        return ans