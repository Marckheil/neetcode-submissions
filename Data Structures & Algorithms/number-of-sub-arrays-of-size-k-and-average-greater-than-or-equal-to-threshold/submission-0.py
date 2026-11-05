class Solution:
	def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
		res = 0
		cur = sum(arr[:k])
		if cur >= threshold * k:
			res += 1

		for R in range(k, len(arr)):
			cur += arr[R]
			cur -= arr[R - k]
			if cur >= threshold * k:
				res += 1

		return res