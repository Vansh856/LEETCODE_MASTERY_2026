class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_hight=0
        curr_hight=0
        for height in gain:
            curr_hight+=height
            max_hight=max(curr_hight,max_hight)
        return max_hight