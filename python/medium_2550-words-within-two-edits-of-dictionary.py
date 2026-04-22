class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        for q in queries:
            for d in dictionary:
                diff = sum(1 for a, b in zip(q, d) if a != b)
                if diff <= 2:
                    res.append(q)
                    break
                    
        return res   