class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sor=defaultdict(list)

        for i in strs:
            temp=''.join(sorted(i))
            sor[temp].append(i)

        return list(sor.values())