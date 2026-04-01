class Solution:
    def isValid(self, s: str) -> bool:

        st=[]
        op=["[","{","("]
        if len(s)%2!=0:
            return False
        
        for i in range(len(s)):
            if s[i] in op:
                st.append(s[i])
            else:
                if st:
                    cl=st.pop()
                    if s[i]==")" and cl=="(":
                        continue
                    elif s[i]=="}" and cl=="{":
                        continue
                    elif s[i]=="]" and cl=="[":
                        continue
                    else:
                        return False
                return False
        if st:
            return False
        return True