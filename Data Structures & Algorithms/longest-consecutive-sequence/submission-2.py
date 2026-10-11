class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = set(nums)
        best = 0
        for num in count:
            if num - 1 not in count:
                longest = 1
                while num+longest in count:
                    longest += 1
            best = max(longest, best )
        return best
    


