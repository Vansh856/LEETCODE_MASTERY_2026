class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new={}
        for i in range(len(nums)):
            sol=target-nums[i]
            if sol in new:
                return [new[sol],i]
            new[nums[i]]=i