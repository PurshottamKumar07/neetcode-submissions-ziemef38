class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result=[0]*len(temperatures)
        st=[]

        for i in range(len(temperatures)-1,0,-1):
            if temperatures[i]>temperatures[i-1]:
                st.append([temperatures[i],i])
        
        i=0
        while st:
            if i>=st[-1][1]:
                st.pop()
            if st and st[-1][0]>temperatures[i]:   
                result[i]=st[-1][1]-i
            elif st:
                for j in range(len(st)-1,-1,-1):
                    if st[j][0]>temperatures[i]:
                        result[i]=st[j][1]-i
                        break
                        
            i+=1

        return result
