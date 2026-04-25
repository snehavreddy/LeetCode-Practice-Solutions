class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        L = moves.count('L')
        R = moves.count('R')
        blank = moves.count('_')
        
        return max(abs(L + blank - R), abs(R + blank - L))