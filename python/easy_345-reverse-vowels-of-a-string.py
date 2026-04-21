class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1
        s_list = list(s)
        while left < right:
            if not self.isVowel(s_list[left]):
                left += 1
            elif not self.isVowel(s_list[right]):
                right -= 1
            else:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        return "".join(s_list)

    def isVowel(self, char: str) -> bool:
        return char.lower() in 'aeiou'