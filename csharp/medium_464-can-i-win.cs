public class Solution {
    Dictionary<int, bool> memo = new Dictionary<int, bool>();

    public bool CanIWin(int maxChoosableInteger, int desiredTotal) {
        if (desiredTotal <= 0) return true;

        int sum = (maxChoosableInteger * (maxChoosableInteger + 1)) / 2;
        if (sum < desiredTotal) return false;

        return dfs(maxChoosableInteger, desiredTotal, 0);
    }

    private bool dfs(int max, int total, int usedMask) {
        if (memo.ContainsKey(usedMask)) 
            return memo[usedMask];

        for (int i = 1; i <= max; i++) {
            int bit = 1 << i;

            if ((usedMask & bit) == 0) { // not used
                // If I win immediately OR opponent loses
                if (i >= total || !dfs(max, total - i, usedMask | bit)) {
                    memo[usedMask] = true;
                    return true;
                }
            }
        }

        memo[usedMask] = false;
        return false;
    }
}