class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_index = -1

class Solution:
    def stringIndices(self, wordsContainer: list[str], wordsQuery: list[str]) -> list[int]:
        root = TrieNode()
        
        # 1. Find the global default best index (shortest, then earliest)
        # This covers the case where a query has 0 common suffix characters.
        global_best_idx = 0
        for i in range(1, len(wordsContainer)):
            if len(wordsContainer[i]) < len(wordsContainer[global_best_idx]):
                global_best_idx = i
                
        root.best_index = global_best_idx
        
        # 2. Build the Trie with reversed words
        for idx, word in enumerate(wordsContainer):
            curr = root
            # Traverse backwards to handle suffixes as prefixes
            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                
                # Update the best index at this node if the current word is a better fit
                if curr.best_index == -1:
                    curr.best_index = idx
                else:
                    curr_best_len = len(wordsContainer[curr.best_index])
                    if len(word) < curr_best_len:
                        curr.best_index = idx
                    # If lengths are equal, the earlier index (curr.best_index) naturally wins
        
        # 3. Process the queries
        ans = []
        for query in wordsQuery:
            curr = root
            # Trace the reversed query down the Trie
            for char in reversed(query):
                if char in curr.children:
                    curr = curr.children[char]
                else:
                    break  # Stop as soon as the common suffix breaks
            
            # The node we land on holds the index of the optimal matching word
            ans.append(curr.best_index)
            
        return ans