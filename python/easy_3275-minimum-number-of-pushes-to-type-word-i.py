class Solution:

  def minimumPushes(self, word: str) -> int:
    n = len(word)
    ans = 0

    for i in range(n):
      # Every 8 characters, the cost per character increases by 1 (1st group of 8 costs 1, 2nd costs 2, etc.)
      ans += (i // 8) + 1

    return ans