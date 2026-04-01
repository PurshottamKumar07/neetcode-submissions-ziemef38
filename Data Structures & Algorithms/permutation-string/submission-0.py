class Solution:
    def checkInclusion(self, s1: str, s2: str):

        cc=Counter(s1)
        check=defaultdict(int)
        a,b=0,len(s1)

        if len(s1)>len(s2):
            return False

        for i in range(len(s1)):
            check[s2[i]]+=1

        while b<len(s2):
            if check==cc:
                return True
            check[s2[b]]+=1
            if check[s2[a]]==1:
                del check[s2[a]]
            else:
                check[s2[a]]-=1
            b+=1
            a+=1

        return cc==check