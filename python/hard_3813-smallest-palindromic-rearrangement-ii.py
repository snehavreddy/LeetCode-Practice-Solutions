from collections import Counter
from math import comb

class Solution:
    LIMIT = 10**6 + 1

    def count_perms(self, cnt):
        total = sum(cnt)
        ans = 1
        rem = total

        for f in cnt:
            if f == 0:
                continue
            ans *= comb(rem, f)
            if ans >= self.LIMIT:
                return self.LIMIT
            rem -= f

        return ans

    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        half_cnt = [0] * 26
        mid = ""
        half_len = 0

        for i in range(26):
            ch = chr(ord('a') + i)
            if ch in freq:
                half_cnt[i] = freq[ch] // 2
                half_len += half_cnt[i]
                if freq[ch] % 2:
                    mid = ch

        if self.count_perms(half_cnt) < k:
            return ""

        left = []

        for _ in range(half_len):
            for i in range(26):
                if half_cnt[i] == 0:
                    continue

                half_cnt[i] -= 1
                ways = self.count_perms(half_cnt)

                if ways >= k:
                    left.append(chr(ord('a') + i))
                    break

                k -= ways
                half_cnt[i] += 1

        left = "".join(left)
        return left + mid + left[::-1]