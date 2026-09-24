class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        emptyArr = []
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        for i in range(k):
            max_key = max(hashMap, key=hashMap.get)
            emptyArr.append(max_key)
            del hashMap[max_key]
        return emptyArr
        

                

