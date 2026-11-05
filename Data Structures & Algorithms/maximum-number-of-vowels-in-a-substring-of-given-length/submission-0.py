class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        count = 0
        for char in range(k):
            if s[char] in vowels:
                count += 1
        bestCount = count
        bestStart = 0

        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i-k] in vowels:
                count -= 1
            if count > bestCount:
                bestCount = count
                bestStart = i-k+1
        return bestCount
