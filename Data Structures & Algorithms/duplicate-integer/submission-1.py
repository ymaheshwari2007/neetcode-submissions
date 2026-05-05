class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited_num = []
        for num in nums:
            if num in visited_num:
                return True
            visited_num.append(num)
        return False
        