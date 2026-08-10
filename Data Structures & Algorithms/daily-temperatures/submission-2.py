class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        l=len(temperatures)
        result=[0]*l
        st=[]
        st.append([temperatures[0],0])

        for i in range(1,l):
            while st and st[-1][0]<temperatures[i]:
                t,j=st.pop()
                result[j]=i-j

            st.append([temperatures[i],i])


        return result