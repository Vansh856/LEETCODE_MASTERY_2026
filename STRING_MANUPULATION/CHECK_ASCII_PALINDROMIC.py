class Solution:
    def isPalindromic(self, s: str) -> bool:
        binary_rep = "".join(f"{ord(c):08b}" for c in s)
        i=0
        j=len(binary_rep)-1
        while i<j:
            if binary_rep[i]!=binary_rep[j]:
                return False
            i+=1
            j-=1
        return True
        