class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
       rev = list(s)
       left, right = 0, len(s) - 1
       while left < right:
        if not rev[left].isalpha():
            left+=1
        elif not rev[right].isalpha():
            right-=1 
        else:
           rev[left], rev[right] = rev[right], rev[left]
           left+=1
           right-=1
       return "".join(rev) 