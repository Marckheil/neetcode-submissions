import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#        count = Counter(nums)
#        buckets = [[] for _ in range(len(nums)+1)]
#        
#        for nums, freq in count.items():
#            buckets[freq].append(nums)
#        res = []
#        for freq in range(len(buckets)-1, 0, -1):
#            for num in buckets[freq]:
#                res.append(num)
#                if len(res) == k:
#                    return res

        nums = Counter(nums)
        lst = []
        for num, freq in nums.items():
            lst.append((-freq, num))

        heapq.heapify(lst)
        res = []
        for _ in range(k):
            freq, num = (heapq.heappop(lst))
            res.append(num)
        
        return res 


             
