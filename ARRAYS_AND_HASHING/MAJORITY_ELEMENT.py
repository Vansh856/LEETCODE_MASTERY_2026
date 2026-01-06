class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sol={}
        for element in nums:
            sol[element]=sol.get(element,0)+1
            if sol[element]>len(nums)/2:
                return element