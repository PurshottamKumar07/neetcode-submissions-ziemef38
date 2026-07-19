class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        temp=-float('inf')
        l=len(s)
        ans=(0,0)

        for k in range(l-1):
            i,j=k,k
            while i>=0 and j<l and s[i]==s[j]:
                if j-i+1>temp:
                    temp=j-i+1
                    ans=(i,j)
                i-=1
                j+=1
            
            i,j=k,k+1
            while i>=0 and j<l and s[i]==s[j]:
                if j-i+1>temp:
                    temp=j-i+1
                    ans=(i,j)
                i-=1
                j+=1
        
        return s[ans[0]:ans[1]+1]