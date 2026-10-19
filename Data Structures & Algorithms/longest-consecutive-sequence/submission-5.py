class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        best = 0                              # NEW: best run seen so far

        for x in setNums:                     # FIX 1: loop over values, not indices
            if x - 1 not in setNums:          # your idea: x is a start
                start = x
                count = 1                     # FIX 4: a lone start is length 1

                while start + 1 in setNums:   # FIX 2: moved inside, runs per start
                    start += 1                # FIX 3: walk forward
                    count += 1

                best = max(best, count)       # FIX 4: keep the longest

        return best