class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Result = set()
        for i in nums:
            if i not in Result: 
                Result.add(i)
            else:
                return True
        return False