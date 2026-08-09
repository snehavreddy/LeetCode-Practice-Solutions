class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        i = 0
        word1Len = len(word1)
        word2Len = len(word2)
        
        while i < word1Len or i < word2Len:
            if i < word1Len:
                result += word1[i]
            if i < word2Len:
                result += word2[i]
            i += 1
            
        return result