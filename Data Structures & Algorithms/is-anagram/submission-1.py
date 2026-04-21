class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for letterS, letterT in zip(sorted(s), sorted(t)):
            if letterS != letterT:
                return False
        return True
