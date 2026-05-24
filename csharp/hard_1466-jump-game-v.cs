public class Solution {
    private int[] dp;
    private int n;

    public int MaxJumps(int[] arr, int d) {
        n = arr.Length;
        dp = new int[n]; // Initialized to 0 by default
        int maxVisits = 0;

        // Try starting from every possible index and find the global maximum
        for (int i = 0; i < n; i++) {
            maxVisits = Math.Max(maxVisits, DFS(arr, i, d));
        }
        return maxVisits;
    }
    private int DFS(int[] arr, int i, int d) {
        // If already calculated, return the cached result
        if (dp[i] != 0) {
            return dp[i];
        }

        int currentMax = 1; // You can always at least visit the current index itself

        // 1. Jump Right: i + x where 1 <= x <= d
        for (int x = 1; x <= d && i + x < n; x++) {
            // If blocked by a taller or equal building, we can't jump further right
            if (arr[i + x] >= arr[i]) {
                break;
            }
            currentMax = Math.Max(currentMax, 1 + DFS(arr, i + x, d));
        }

        // 2. Jump Left: i - x where 1 <= x <= d
        for (int x = 1; x <= d && i - x >= 0; x++) {
            // If blocked by a taller or equal building, we can't jump further left
            if (arr[i - x] >= arr[i]) {
                break;
            }
            currentMax = Math.Max(currentMax, 1 + DFS(arr, i - x, d));
        }

        // Save the result to the memoization array
        dp[i] = currentMax;
        return dp[i];
    }

}