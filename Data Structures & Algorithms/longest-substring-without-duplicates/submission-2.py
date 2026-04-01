class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ans=1
        a=0
        ver=[]
        if len(s)<2:
            return len(s)

        for i in range(len(s)):
            while s[i] in ver:
                ver.pop(0)
                a+=1
            ver.append(s[i])
            ans=max(ans,len(ver))
        
        return ans