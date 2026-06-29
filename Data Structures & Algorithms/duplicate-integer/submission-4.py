class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newSet = set()
        for num in nums:
            newSet.add(num)
        if len(nums) != len(newSet):
            return True
        return False