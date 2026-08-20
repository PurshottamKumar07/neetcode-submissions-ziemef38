class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        src=defaultdict(set)

        for i,j in prerequisites:
            src[i].add(j)
        
        temp=set()
        path=set()
        
        def dfs(n):
            if n in temp:
                return True

            if n in path:
                return False

            if n not in src:
                return True

            path.add(n)
            for i in src[n]:
                if not dfs(i):
                    return False
            
            path.remove(n)
            temp.add(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True