class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        i=0
        num=0
        s=sum(nums)
        for j in range(len(nums)):
            if s-num-nums[j]==num:
                return j
            else:
                num+=nums[j]
        return -1
