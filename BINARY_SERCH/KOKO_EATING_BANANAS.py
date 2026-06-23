from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def feasible(speed) -> bool:
            # Sahi aur tez integer division formula: (pile + speed - 1) // speed
            return sum((pile + speed - 1) // speed for pile in piles) <= H

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid  # Mid speed feasible hai, toh aur kam speed check karo
            else:
                left = mid + 1  # Speed bohot kam hai, badhana padega
        return left