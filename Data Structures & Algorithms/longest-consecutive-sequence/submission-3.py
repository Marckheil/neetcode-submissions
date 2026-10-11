class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0
        for x in s:
            if x - 1 not in s:              # x starts a run (nothing before it)
                length = 1
            while x + length in s:      # walk forward while the run continues
                length += 1
            best = max(best, length)
        return best