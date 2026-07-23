class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Find the most significant bit (MSB) of n
        msb = n.bit_length() - 1
        return (1 << (msb + 1))