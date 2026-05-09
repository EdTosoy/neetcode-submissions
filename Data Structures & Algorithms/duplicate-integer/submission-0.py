class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setVersion = set(nums)
        if len(setVersion) < len(nums):
            return True
        return False