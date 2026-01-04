class Solution:
    def isPalindrome(self, x: int) -> bool:
        strn=str(x)
        right=0
        left=len(strn)-1
        while left>right:
            if strn[left]==strn[right]:
                right+=1
                left-=1
            else:
                return False
        return True
        