class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currentBest = 0
        counter = 0
        for x in nums:
            if x == 1:
                counter += 1
                currentBest = max(currentBest, counter)
            else:
                counter = 0
        return max(currentBest, counter)
            
                
                
