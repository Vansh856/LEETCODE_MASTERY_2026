class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        squaresum=0
        digisum=0
        while n!=0:
            digi=n%10
            squaresum+=digi**2
            digisum+=digi
            n=n//10
        if squaresum-digisum>=50:
            return True
        return False