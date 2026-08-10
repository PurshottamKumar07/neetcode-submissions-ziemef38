class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        l=len(position)
        
        sor=sorted(zip(position , speed))

        st=[]
        temp=(target-sor[0][0])/sor[0][1]
        st.append(temp)
        ans=0

        for p,s in sor:
            temp=(target-p)/s

            while st and st[-1]<=temp:
                st.pop()
            st.append(temp)
        
        return len(st)