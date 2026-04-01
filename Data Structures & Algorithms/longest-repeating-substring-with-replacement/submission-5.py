class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq={}
        ans=0
        l=0
        for r in range(len(s)):
            if s[r] not in freq.keys():
                freq[s[r]]=0
            freq[s[r]]+=1

            count=r-l+1

            while count-max(freq.values())>k:
                freq[s[l]]-=1
                l+=1
                count=r-l+1
                
            ans=max(count,ans)
        return ans

