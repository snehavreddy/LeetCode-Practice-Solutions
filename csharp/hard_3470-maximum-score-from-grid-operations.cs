public class Solution {
    public long MaximumScore(int[][] grid) {
        int n = grid.Length;
        // Precompute prefix sums for each column to calculate segment sums in O(1)
        long[][] pref = new long[n][];
        for (int j = 0; j < n; j++) {
            pref[j] = new long[n + 1];
            for (int i = 0; i < n; i++) {
                pref[j][i + 1] = pref[j][i] + grid[i][j];
            }
        }

        // Helper to get sum of grid[l...r] in column j
        long Get(int j, int l, int r) {
            if (l > r) return 0;
            return pref[j][r + 1] - pref[j][l];
        }

        // prevPick[h] stores max score if previous column had height h
        // prevSkip[h] tracks the alternate state to handle transitions
        long[] prevPick = new long[n + 1];
        long[] prevSkip = new long[n + 1];

        // Initialize for the first column (column 0)
        for (int h = 0; h <= n; h++) {
            prevPick[h] = 0;
            prevSkip[h] = 0;
        }

        for (int j = 1; j < n; j++) {
            long[] currPick = new long[n + 1];
            long[] currSkip = new long[n + 1];
            for (int h = 0; h <= n; h++) {
                currPick[h] = long.MinValue;
                currSkip[h] = long.MinValue;
            }

            for (int curr = 0; curr <= n; curr++) {
                for (int prev = 0; prev <= n; prev++) {
                    if (curr > prev) {
                        // Current height is greater than previous; add score from column j-1
                        long score = Get(j - 1, prev, curr - 1);
                        currPick[curr] = Math.Max(currPick[curr], prevSkip[prev] + score);
                        currSkip[curr] = Math.Max(currSkip[curr], prevSkip[prev] + score);
                    } else {
                        // Previous height is greater or equal; add score from column j
                        long score = Get(j, curr, prev - 1);
                        currPick[curr] = Math.Max(currPick[curr], prevPick[prev] + score);
                        currSkip[curr] = Math.Max(currSkip[curr], prevPick[prev]);
                    }
                }
            }
            prevPick = currPick;
            prevSkip = currSkip;
        }

        long ans = 0;
        for (int h = 0; h <= n; h++) {
            ans = Math.Max(ans, Math.Max(prevPick[h], prevSkip[h]));
        }
        return ans;
    }
}