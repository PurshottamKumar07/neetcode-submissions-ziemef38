class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
    
        st=[]

        for i in tokens:
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
            elif i=="/":
                a=st.pop()
                b=st.pop()
                st.append(int(b/a))
            else:
                st.append(int(i))

        return st[-1]