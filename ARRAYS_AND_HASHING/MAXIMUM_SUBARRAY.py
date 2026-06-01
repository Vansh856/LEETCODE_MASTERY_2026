class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 1. Initialization: -inf ki jagah pehle element se start karein
        max_sum = nums[0]
        current_sum = 0
        
        for n in nums:
            # 2. Sum update karein
            current_sum += n
            
            # 3. Kya humne naya record banaya? (Fast 'if' instead of max())
            if current_sum > max_sum:
                max_sum = current_sum
            
            # 4. RESET: Agar sum negative ho jaye, toh aage ke liye bojh hai. 
            # Use 0 kar do taaki agla element ek fresh start kare.
            if current_sum < 0:
                current_sum = 0
                
        return max_sum