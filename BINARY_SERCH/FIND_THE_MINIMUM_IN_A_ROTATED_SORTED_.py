class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        sol=nums[0]
        while low<=high:
            mid=(low+high)//2
            sol=min(nums[mid],sol)
            if nums[mid]<nums[high]:
                high=mid-1
            else:
                low=mid+1
        return sol
        