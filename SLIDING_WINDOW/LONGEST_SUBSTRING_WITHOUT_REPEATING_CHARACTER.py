class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=1
        sol=set()
        l=0
        if s=="":
            return 0
        for i in range(len(s)):
            while s[i] in sol:
                sol.remove(s[l])
                l+=1
            sol.add(s[i])
            if len(sol)>length:
                length=len(sol)
        return length                