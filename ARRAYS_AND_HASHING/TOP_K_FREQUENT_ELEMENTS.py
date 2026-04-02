class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sol={}
        for elements in nums:
            sol[elements]=sol.get(elements,0)+1
        sorted_list = sorted(sol.items(), key=lambda item: item[1], reverse=True)
        return [iteam[0] for iteam in sorted_list[:k]]