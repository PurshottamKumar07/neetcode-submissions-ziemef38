class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic=defaultdict(list)

        for i in range(len(strs)):
            temp=tuple(sorted(strs[i]))
            dic[temp].append(strs[i])
        
        ans=[]
        for i,j in dic.items():
            ans.append(j)
        
        return ans