class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count=defaultdict(int)
        window=defaultdict(int)
        if len(s1)>len(s2):
            return False
        for i in range(len(s1)):
            s1_count[s1[i]]+=1
            window[s2[i]]+=1
        left=0
        right=len(s1)-1
        while right<len(s2):
            if s1_count==window:
                return True
            else:
                right+=1
                if right<len(s2):
                    window[s2[right]]+=1
                    window[s2[left]]-=1
                    if window[s2[left]]==0:
                        del window[s2[left]]
                    left+=1
        return False