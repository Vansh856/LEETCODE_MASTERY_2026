class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        result=[]
        num=set(nums)
        curr_range=[]
        for i in range(lower,upper+1):
            
            if i not in num:
                curr_range.append(i)
            elif curr_range:
                result.append([curr_range[0],curr_range[-1]])
                curr_range=[]
        if curr_range:
            result.append([curr_range[0],curr_range[-1]])
        return result