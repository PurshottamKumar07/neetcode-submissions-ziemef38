class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: return "❌"
        enc="😀".join(strs)
        return enc

    def decode(self, s: str) -> List[str]:
        if s == "❌": return []
        dec=[]
        a=0
        for i in range(len(s)):
            if s[i]=="😀":
                dec.append(s[a:i])
                a=i+1
        dec.append(s[a:])
        return dec