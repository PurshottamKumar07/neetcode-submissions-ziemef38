class Solution:
    def countSubstrings(self, s: str) -> int:
        
        l=len(s)
        dp=[[False]*(l) for _ in range(l)]
        ans=0

        for i in range(l-1,-1,-1):
            for j in range(i,l):
                if s[i]==s[j]:
                    if j-i<=1 :
                        dp[i][j]=True
                    elif dp[i+1][j-1]:
                        dp[i][j]=True
                if dp[i][j]:
                    ans+=1

        return ans