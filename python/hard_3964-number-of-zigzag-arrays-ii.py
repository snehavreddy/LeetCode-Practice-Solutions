class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        if n == 1:
            return r - l + 1
        
        MOD = 10**9 + 7
        m = r - l + 1
        
        # Build the transition matrix T of size 2m x 2m.
        # States 0 to m-1: "up" (next must be smaller)
        # States m to 2m-1: "down" (next must be larger)
        size = 2 * m
        T = [[0] * size for _ in range(size)]
        
        # From "up" at value x, we can go to "down" at value y < x
        for x in range(m):
            for y in range(x):
                T[y + m][x] = 1
        
        # From "down" at value x, we can go to "up" at value y > x
        for x in range(m):
            for y in range(x + 1, m):
                T[y][x + m] = 1
                
        def multiply(A, B):
            C = [[0] * size for _ in range(size)]
            for i in range(size):
                for k in range(size):
                    if A[i][k] == 0: continue
                    for j in range(size):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            return C
            
        def power(A, p):
            res = [[0] * size for _ in range(size)]
            for i in range(size): res[i][i] = 1
            while p > 0:
                if p % 2 == 1: res = multiply(res, A)
                A = multiply(A, A)
                p //= 2
            return res
            
        # T^(n-1)
        T_n_minus_1 = power(T, n - 1)
        
        # Initial vector: sum of all possible states at length 1 (which are 1)
        # Starting with either "up" or "down" covers all first pairs
        ans = 0
        for i in range(size):
            for j in range(size):
                ans = (ans + T_n_minus_1[i][j]) % MOD
                
        return ans