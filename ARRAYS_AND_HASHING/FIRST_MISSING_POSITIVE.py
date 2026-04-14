class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Har number ko uske sahi index par bhejo
        # Number 'x' ka sahi index 'x - 1' hota hai
        for i in range(n):
            # Jab tak current number valid hai aur apni sahi jagah par nahi hai
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with the number at its target index
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
        
        # 

        # Step 2: Check karo kaunsa index apne number se match nahi kar raha
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # Agar saare 1 se n tak present hain, toh missing n + 1 hoga
        return n + 1