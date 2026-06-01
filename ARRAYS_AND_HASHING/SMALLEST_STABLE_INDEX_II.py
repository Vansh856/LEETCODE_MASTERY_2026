class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maxi=nums[0]
        n = len(nums)
        mini=nums[n-1]
        max_array=[0]*n
        
        for i in range(len(nums)):
            if maxi<nums[i]:
                maxi=nums[i]
            max_array[i]=maxi
        min_array=[0]*n
        for i in range(n-1,-1,-1):
            if mini>nums[i]:
                mini=nums[i]
            min_array[i]=mini
            
        
        for i in range(n):
            if max_array[i]-min_array[i]<=k:
                return i
        return -1