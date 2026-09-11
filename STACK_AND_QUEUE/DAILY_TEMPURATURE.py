class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        curr=[]
        ans=[0]*len(temperatures)
        for i in range(len(temperatures)):

            while curr and temperatures[i]>temperatures[curr[-1]]:
                ans[curr[-1]]=i-curr[-1]
                curr.pop()
            curr.append(i)
        
        return ans