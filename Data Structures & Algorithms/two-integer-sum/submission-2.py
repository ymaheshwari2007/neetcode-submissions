class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i,j in enumerate(nums):
            t = target - j
            if t in h:
                return [h[t],i]
            else:
                h[j] = i
