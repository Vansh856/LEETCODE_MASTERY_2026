class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        result=0
        while i<j:
            curr=(nums[i]-1)*(nums[j]-1)
            result=max(curr,result)
            if nums[i]>nums[j]:
                j-=1
            else:
                i+=1
        
        return result

        