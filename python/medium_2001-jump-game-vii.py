from collections import deque

class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """

        n = len(s)

        q = deque([0])

        far = 1

        while q:

            i = q.popleft()

            start = max(i + minJump, far)
            end = min(i + maxJump, n - 1)

            for j in range(start, end + 1):

                if s[j] == '0':

                    if j == n - 1:
                        return True

                    q.append(j)

            far = end + 1

        return n == 1       