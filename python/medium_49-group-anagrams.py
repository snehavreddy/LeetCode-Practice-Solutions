class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))   # sort letters
            groups[key].append(word)      # group words

        return list(groups.values())