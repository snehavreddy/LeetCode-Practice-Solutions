class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7
        
        # dp_score[i][j] stores the max score to reach (i, j)
        # dp_count[i][j] stores the number of ways to reach (i, j) with max score
        dp_score = [[-1] * n for _ in range(n)]
        dp_count = [[0] * n for _ in range(n)]
        
        # Starting point is bottom-right 'S'
        dp_score[n - 1][n - 1] = 0
        dp_count[n - 1][n - 1] = 1
        
        # Traverse backwards from (n-1, n-1) to (0, 0)
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X' or dp_score[i][j] == -1:
                    continue
                
                # Possible moves: up (i-1, j), left (i, j-1), up-left (i-1, j-1)
                for di, dj in [(0, -1), (-1, 0), (-1, -1)]:
                    ni, nj = i + di, j + dj
                    
                    if ni >= 0 and nj >= 0 and board[ni][nj] != 'X':
                        # Get value of the cell
                        val = 0
                        if board[ni][nj] != 'E':
                            val = int(board[ni][nj])
                        
                        new_score = dp_score[i][j] + val
                        
                        if new_score > dp_score[ni][nj]:
                            dp_score[ni][nj] = new_score
                            dp_count[ni][nj] = dp_count[i][j]
                        elif new_score == dp_score[ni][nj]:
                            dp_count[ni][nj] = (dp_count[ni][nj] + dp_count[i][j]) % MOD
                            
        if dp_score[0][0] == -1:
            return [0, 0]
        else:
            return [dp_score[0][0], dp_count[0][0]]