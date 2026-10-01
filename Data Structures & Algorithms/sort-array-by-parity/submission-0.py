class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        newArr = []
        oddArr = []
        for num in nums:
            if num % 2 == 0:
                newArr.append(num)
            else:
                oddArr.append(num)
            
        return newArr + oddArr