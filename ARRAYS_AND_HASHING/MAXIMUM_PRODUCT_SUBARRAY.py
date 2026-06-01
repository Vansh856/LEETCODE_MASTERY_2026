class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curr_min,curr_max=1,1
        for i in nums:
            temp=curr_max * i
            curr_max=max(curr_max * i,curr_min*i,i)
            curr_min=min(temp,curr_min*i,i)
            res=max(res,curr_max)
        return res
