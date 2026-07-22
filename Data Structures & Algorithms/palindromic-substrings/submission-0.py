class Solution:
    def countSubstrings(self, s: str) -> int:
        
        l=len(s)
        ans=0

        for i in range(l):
            a,b=i,i
            while b<len(s) and a>=0 and s[a]==s[b]:
                ans+=1
                a-=1
                b+=1
            
            a,b=i,i+1
            while b<len(s) and a>=0 and s[a]==s[b]:
                ans+=1
                a-=1
                b+=1

        return ans
            