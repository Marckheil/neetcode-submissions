class Solution:
    def findMin(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] <= nums[-1]:
                hi = mid
            else:
                lo = mid + 1

        return nums[lo]