from collections import defaultdict


class Solution:

  def maxSubarrayLength(self, nums: list[int], k: int) -> int:
    freq = defaultdict(int)
    left = 0
    max_length = 0

    for right in range(len(nums)):
      # Expand the window by adding the current element
      freq[nums[right]] += 1

      # Shrink the window if the frequency of the current element exceeds k
      while freq[nums[right]] > k:
        freq[nums[left]] -= 1
        left += 1

      # Update the maximum length found so far
      max_length = max(max_length, right - left + 1)

    return max_length