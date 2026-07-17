class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count=0
        for alpha in patterns:
            if alpha in word:
                count+=1
        return count