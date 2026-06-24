class Solution:
    def processStr(self, s: str) -> str:
        result=""
        for word in s:
            if word=="*":
                result=result[:-1]

            elif word=="#":
                result+=result

            elif word=="%":
                result=result[::-1]

            else:
                result+=word
        return result