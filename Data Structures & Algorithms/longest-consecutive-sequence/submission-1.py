class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num-1 not in numSet:
                best = 1
                current = num
                while current + 1 in numSet:
                    current += 1
                    best += 1
                longest = max(longest, best)
        return longest
        