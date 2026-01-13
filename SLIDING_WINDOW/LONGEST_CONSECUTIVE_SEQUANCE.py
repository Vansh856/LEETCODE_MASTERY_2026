class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans=set(nums)
        lengths=0
        for i in ans:
            if i-1 not in ans:
                length=1
                while i+length in ans:
                    length+=1
                lengths=max(lengths,length)

        return lengths