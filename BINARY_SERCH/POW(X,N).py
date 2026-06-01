class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pov(x,n):
            if n==0:
                return 1
            if x==0:
                return 0
            if n<0:
                return 1/pov(x,-n)
            if x==1:
                return 1
            half=pov(x,n//2)

            if n%2==0:
                return half*half
            else:
                return half*half*x
        return pov(x,n)