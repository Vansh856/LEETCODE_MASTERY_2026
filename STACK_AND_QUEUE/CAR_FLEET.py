class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        
        stack = []
        for pos, spd in pair:
            time = (target - pos) / spd
            
            # Agar stack empty hai ya yeh car aage wale fleet se slow hai,
            # toh yeh aage wali se kabhi merge nahi hogi -> Naya fleet banega
            if not stack or time > stack[-1]:
                stack.append(time)
                
        return len(stack)