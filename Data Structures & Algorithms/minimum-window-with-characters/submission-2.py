class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        ver=Counter(t)
        check=defaultdict(int)

        x=len(ver)
        y=0
         
        temp=float('inf')
        l=0
        ans=[0,0]

        if len(s)<len(t):
            return ""

        for i in range(len(s)):
            check[s[i]]+=1

            if s[i] in ver and ver[s[i]]==check[s[i]]:
                y+=1
            
            while x==y:
                check[s[l]]-=1

                if s[l] in ver and ver[s[l]]>check[s[l]]:
                    y-=1
                    if temp>i-l+1:
                        temp=i-l+1
                        ans[0],ans[1]=l,i
                l+=1
           
        
        return s[ans[0]:ans[1]+1] if temp!=float('inf') else ""