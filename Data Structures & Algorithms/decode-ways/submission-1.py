class Solution:
    def numDecodings(self, s: str) -> int:
        
        l=len(s)

        def rec(n,memo):
            if n==l:
                return 1
            
            if n in memo:
                return memo[n]

            if s[n]=="0":
                return 0
            ans=0
            ans+=rec(n+1,memo)
            if n+1<l and (0<int(s[n:n+2])<27):
                ans+= rec(n+2,memo)
            
            memo[n]=ans
            return ans
            
        return rec(0,{})