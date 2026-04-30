public class Solution {
    public int MaxPathScore(int[][] grid, int k) {
        int m = grid.Length, n = grid[0].Length;

        int[,,] dp = new int[m, n, k + 1];

        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                for (int c = 0; c <= k; c++)
                    dp[i, j, c] = -1;

        dp[0, 0, 0] = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {

                for (int c = 0; c <= k; c++) {
                    if (dp[i, j, c] == -1) continue;

                    // DOWN
                    if (i + 1 < m) {
                        int val = grid[i + 1][j];
                        int nc = c + (val == 0 ? 0 : 1);
                        if (nc <= k) {
                            int ns = dp[i, j, c] + val;
                            dp[i + 1, j, nc] = Math.Max(dp[i + 1, j, nc], ns);
                        }
                    }

                    // RIGHT
                    if (j + 1 < n) {
                        int val = grid[i][j + 1];
                        int nc = c + (val == 0 ? 0 : 1);
                        if (nc <= k) {
                            int ns = dp[i, j, c] + val;
                            dp[i, j + 1, nc] = Math.Max(dp[i, j + 1, nc], ns);
                        }
                    }
                }
            }
        }

        int ans = -1;
        for (int c = 0; c <= k; c++) {
            ans = Math.Max(ans, dp[m - 1, n - 1, c]);
        }

        return ans;
    }
}