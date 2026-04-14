class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # A hamesha choti array honi chahiye
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
            
        total = len(A) + len(B)
        half = (total + 1) // 2
        
        low, high = 0, len(A)
        
        while low <= high:
            cut1 = (low + high) // 2
            cut2 = half - cut1
            
            # Boundary values (Handle -infinity and +infinity for edge cases)
            L1 = A[cut1 - 1] if cut1 > 0 else float("-infinity")
            R1 = A[cut1] if cut1 < len(A) else float("infinity")
            L2 = B[cut2 - 1] if cut2 > 0 else float("-infinity")
            R2 = B[cut2] if cut2 < len(B) else float("infinity")
            
            # Perfect partition mil gaya?
            if L1 <= R2 and L2 <= R1:
                if total % 2:
                    return max(L1, L2)
                return (max(L1, L2) + min(R1, R2)) / 2
            
            elif L1 > R2:
                high = cut1 - 1 # Cut thoda piche le jao
            else:
                low = cut1 + 1  # Cut thoda aage le jao