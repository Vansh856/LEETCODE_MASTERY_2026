import math

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        def is_prime(n):
            if n <= 1: return False
            if n <= 3: return True
            if n % 2 == 0 or n % 3 == 0: return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

        total_ops = 0
        for i in range(len(nums)):
            current_val = nums[i]
            
            if i % 2 == 0: # Element should be Prime
                while not is_prime(current_val):
                    current_val += 1
                    total_ops += 1
            else: # Element should be Non-Prime
                while is_prime(current_val):
                    current_val += 1
                    total_ops += 1
                    
        return total_ops