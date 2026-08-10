class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        l=len(temperatures)
        result=[0]*l
        st=[]
        st.append(0)

        for i in range(1,l):
            while st and temperatures[st[-1]]<temperatures[i]:
                j=st.pop()
                result[j]=i-j

            st.append(i)


        return result