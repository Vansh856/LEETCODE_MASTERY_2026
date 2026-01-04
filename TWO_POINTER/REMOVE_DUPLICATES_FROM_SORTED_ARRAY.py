class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        k=1
        for j in range(1,len(nums)):
        
            if nums[i]!= nums[j]:
                i+=1
                nums[i]=nums[j]
               
                k+=1
        return k

