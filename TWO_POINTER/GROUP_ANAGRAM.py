class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicto=defaultdict(list)
        for s in strs:
            key="".join(sorted(s))
            dicto[key].append(s)

        return list(dicto.values())
        