class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s)<len(t):
            return ""
        
        ver=Counter(t)
        tv=defaultdict(int)

        formed=0
        require=len(ver)
        
        ans=float('inf')
        res=(0,0)

        l=0
        for r in range(len(s)):
            tv[s[r]]+=1

            if s[r] in ver and tv[s[r]]==ver[s[r]]:
                formed+=1

            while formed==require:
                if r-l<ans:
                    ans=r-l
                    res=(l,r)

                tv[s[l]]-=1

                if s[l] in ver and tv[s[l]]<ver[s[l]]:
                    formed-=1
                l+=1

        return "" if ans==float("inf") else s[res[0]:res[1]+1]