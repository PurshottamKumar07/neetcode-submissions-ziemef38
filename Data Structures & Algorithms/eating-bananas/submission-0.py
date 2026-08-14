class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def out(k):
            temp=0
            for i in range(len(piles)):
                temp+=(piles[i]//k)
                if piles[i]%k!=0:
                    temp+=1
            return temp

        def bs(low,high):
            if low>high:
                return low

            mid=(low+high)//2
            output=out(mid)

            if output<=h:
                return bs(low,mid-1)
            else:
                return bs(mid+1,high)
        
        return bs(1,max(piles))