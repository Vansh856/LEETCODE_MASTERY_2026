class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        cost=sorted(costs)
        count=0
        total=0
        for price in cost:
            total+=price
            if total>coins:
                break
            count+=1

        return count