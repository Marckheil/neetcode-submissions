class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        for x in s[:k]:
            if x in 'aeiou':
                count+=1
        best = count
        for i in range(k,len(s)):
            if s[i] in 'aeiou':
                count+=1
            if s[i-k] in 'aeiou':
                count-=1
            best = max(best,count)
        return best
