class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(weight)->bool:
            size=0
            day=1
            for container in weights:
                size+=container
                if size>weight:
                    day+=1
                    size=container
                
            return day<=days

        left=max(weights)
        right=sum(weights)
        while left<right:
            mid=left+(right-left)//2
            if feasible(mid):
                right=mid
            else:
                left=mid+1
        return left