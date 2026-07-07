class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s)<len(t):
            return ""

        ver=Counter(t)
        ts=defaultdict(int)

        l=0
        ans=float('inf')

        formed=0
        tc=len(ver)

        res=(0,0)

        for r in range(len(s)):
            ts[s[r]]+=1

            if s[r] in ver and ts[s[r]]==ver[s[r]]:
                formed+=1
            
            while formed==tc:
                if r-l<ans:
                    ans=r-l
                    res=(l,r)

                ts[s[l]]-=1

                if s[l] in ver and ts[s[l]]<ver[s[l]]:
                    formed-=1
                l+=1
            
        return "" if ans==float('inf') else s[res[0]:res[1]+1] 