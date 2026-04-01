class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        ans=1
        a,b=0,1
        temp=k
        t=1
        if len(s)<2:
            return len(s)

        while a<len(s):
            if b==len(s):
                a+=1
                t+=min(a-1,temp)
                ans=max(ans,t)
                t,b=1,a+1
                temp=k
                continue
            if s[b]==s[a]:
                b+=1
                t+=1
            elif s[b]!=s[a] and temp!=0:
                temp-=1
                t+=1
                b+=1
            else:
                a+=1
                ans=max(ans,t)
                t,b=1,a+1
                temp=k

        return ans