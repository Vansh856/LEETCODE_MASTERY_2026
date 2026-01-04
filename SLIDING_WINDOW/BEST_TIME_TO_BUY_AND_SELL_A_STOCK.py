class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=i+1
        maxp=0
        while j<len(prices):
            if prices[i]>prices[j]:
                i=j
                j+=1
            elif prices[i]<prices[j]:
                maxc=prices[j]-prices[i]
                if maxc>maxp:
                    maxp=maxc
                    j+=1
                else:
                    j+=1
            else:
                i=j
                j+=1
        return maxp