class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach=0
        right=len(nums)-1
        if len(nums)==1:
            return True
        for i in range(len(nums)):
            if i>reach:
                return False
            reach=max(reach,i+nums[i])
            if reach>=right:
                return True
            
        return False