class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_map = defaultdict(list)
        for s in strs:
            new_map[tuple(sorted(s))].append(s)
        return list(new_map.values())