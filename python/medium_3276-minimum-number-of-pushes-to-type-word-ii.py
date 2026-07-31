class Solution:
    def minimumPushes(self, word: str) -> int:
        from collections import Counter
        
        # Count the frequency of each character in the word
        freq = Counter(word)
        
        # Sort frequencies in descending order
        sorted_freq = sorted(freq.values(), reverse=True)
        
        total_pushes = 0
        for i, count in enumerate(sorted_freq):
            # The first 8 frequent characters require 1 push each (multiplier 1)
            # The next 8 require 2 pushes each (multiplier 2), and so on.
            multiplier = (i // 8) + 1
            total_pushes += count * multiplier
            
        return total_pushes