class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sol=[]
        intervals.sort(key=lambda x:x[0])
        prev=intervals[0]
        for interval in intervals:
            if interval[0]<=prev[1]:
                prev[1]=max(prev[1],interval[1])
            else:
                sol.append(prev)
                prev=interval
        sol.append(prev)

        
            
        return sol
