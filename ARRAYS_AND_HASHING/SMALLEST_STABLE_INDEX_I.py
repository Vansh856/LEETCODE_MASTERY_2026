class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        for i in range(n):
            m=max(nums[0:i+1])
            l=min(nums[i:n])
            if (m-l)<=k:
                return i
            
        return -1