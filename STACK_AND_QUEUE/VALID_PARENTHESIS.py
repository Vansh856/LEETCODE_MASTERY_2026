class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        top=-1
        if len(s)%2!=0:
            return False
        for c in s:
            if top==-1:
                top+=1
                stack.append(c)
            elif c==")" and stack[top]=="(":
                top-=1
                stack.pop()
            elif c=="]" and stack[top]=="[":
                top-=1
                stack.pop()
            elif c=="}" and stack[top]=="{":
                top-=1
                stack.pop()
            else:
                top+=1
                stack.append(c)
        return top==-1