class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        temp=[-x for x in stones]
        heapq.heapify(temp)

        while len(temp)>=2:
            f=heapq.heappop(temp)
            s=heapq.heappop(temp)
            if f!=s:
                heapq.heappush(temp,f-s)
        
        if temp:
            return -temp[0]
        return 0