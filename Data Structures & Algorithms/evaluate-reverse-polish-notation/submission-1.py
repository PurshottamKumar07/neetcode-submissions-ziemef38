class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
    
        st=[]

        for i in tokens:
            if i not in "+/-*":
                st.append(int(i))
            else:
                if i=="+":
                    a=st.pop()
                    b=st.pop()
                    st.append(a+b)
                elif i=="-":
                    b=st.pop()
                    a=st.pop()
                    st.append(a-b)
                elif i=="*":
                    a=st.pop()
                    b=st.pop()
                    st.append(a*b)
                else:
                    a=st.pop()
                    b=st.pop()
                    st.append(int(b/a))
            

        return st[-1]