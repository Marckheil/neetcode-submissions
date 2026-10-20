class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        best = 0
        count = {}
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            while count[s[right]] > 1:
                count[s[left]] -= 1
                left += 1
            best = max(best, right-left + 1)
        return best
        
        abcab