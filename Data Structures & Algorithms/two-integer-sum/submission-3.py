class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevSeen = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in prevSeen:
                return [prevSeen[diff], i]
            prevSeen[v] = i
        return []