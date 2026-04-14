public class Solution {
    public long MinimumTotalDistance(IList<int> robot, int[][] factory) {
        int n = robot.Count;
        int m = factory.Length;

        int[] r = robot.ToArray();
        Array.Sort(r);

        Array.Sort(factory, (a, b) => a[0].CompareTo(b[0]));

        long[,] dp = new long[n + 1, m + 1];

        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= m; j++) {
                dp[i, j] = long.MaxValue / 2;
            }
        }

        dp[0, 0] = 0;

        for (int j = 1; j <= m; j++) {
            int pos = factory[j - 1][0];
            int limit = factory[j - 1][1];

            for (int i = 0; i <= n; i++) {
                dp[i, j] = dp[i, j - 1];

                long cost = 0;

                for (int k = 1; k <= limit && k <= i; k++) {
                    cost += Math.Abs(r[i - k] - pos);
                    dp[i, j] = Math.Min(dp[i, j],
                        dp[i - k, j - 1] + cost);
                }
            }
        }

        return dp[n, m];
    }
}