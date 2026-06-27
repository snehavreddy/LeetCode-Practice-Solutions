from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 1

        # Special case for 1
        if 1 in freq:
            if freq[1] % 2 == 0:
                ans = max(ans, freq[1] - 1)
            else:
                ans = max(ans, freq[1])

        for x in freq:
            if x == 1:
                continue

            cur = x
            length = 0

            while cur in freq:
                if freq[cur] >= 2:
                    length += 2
                    cur = cur * cur
                else:
                    length += 1
                    break

            # If we ended because the next square doesn't exist,
            # remove the last pair since there is no center above it.
            if cur not in freq:
                length -= 1

            ans = max(ans, length)

        return ans