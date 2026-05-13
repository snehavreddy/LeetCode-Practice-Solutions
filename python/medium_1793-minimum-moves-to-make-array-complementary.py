class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)

        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):

            a = nums[i]
            b = nums[n - 1 - i]

            x = min(a, b)
            y = max(a, b)

            s = a + b

            # default 2 moves
            diff[2] += 2
            diff[2 * limit + 1] -= 2

            # one move range
            diff[x + 1] -= 1
            diff[y + limit + 1] += 1

            # zero move exact sum
            diff[s] -= 1
            diff[s + 1] += 1

        ans = float('inf')
        cur = 0

        for t in range(2, 2 * limit + 1):
            cur += diff[t]
            ans = min(ans, cur)

        return ans     