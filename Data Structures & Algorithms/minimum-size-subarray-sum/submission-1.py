class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur = 0
        l = 0
        best = float('inf')

        for r in range(len(nums)):
            cur += nums[r]
            while cur >= target:
                best = min(best, r - l + 1)
                cur -= nums[l]
                l += 1
        return best if best != float('inf') else 0

        
            



        