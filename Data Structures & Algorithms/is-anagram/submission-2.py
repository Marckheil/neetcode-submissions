class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        empty_map = {}
        for char in s:
            if char not in empty_map:
                empty_map[char] = 1
            else:
                empty_map[char] += 1
        for char in t:
            if char not in empty_map:
                return False
            else:
                empty_map[char] -= 1
        if all(val == 0 for val in empty_map.values()):
            return True
        return False