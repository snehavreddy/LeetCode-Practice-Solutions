class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = "1" + s + "1"

        segments = []
        i = 0
        while i < len(t):
            j = i
            while j < len(t) and t[j] == t[i]:
                j += 1
            segments.append((t[i], j - i))
            i = j

        ans = s.count("1")
        best = 0

        # Iterate over inner 1-blocks
        for i in range(2, len(segments) - 1, 2):
            best = max(best, segments[i - 1][1] + segments[i + 1][1])

        return ans + best