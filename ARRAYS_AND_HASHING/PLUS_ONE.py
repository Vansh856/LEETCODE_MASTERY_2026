class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strn=""
        for digit in digits:
            strn+=str(digit)
            
        new=int(strn)+1
        return list(map(int,str(new)))

        