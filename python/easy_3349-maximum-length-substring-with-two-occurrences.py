class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        char_count = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            # Expand the window by adding s[right]
            char_count[s[right]] = char_count.get(s[right], 0) + 1

            # Shrink the window until all characters have at most 2 occurrences.
            while char_count[s[right]] > 2:
                char_count[s[left]] -= 1
                left += 1

            # Update maximum valid length found.
            max_len = max(max_len, right - left + 1)

        return max_len