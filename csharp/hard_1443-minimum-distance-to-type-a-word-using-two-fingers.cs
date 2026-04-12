public class Solution {
    
    int Dist(int a, int b) {
        if (a == -1 || b == -1) return 0;
        
        int x1 = a / 6, y1 = a % 6;
        int x2 = b / 6, y2 = b % 6;
        
        return Math.Abs(x1 - x2) + Math.Abs(y1 - y2);
    }
    
    public int MinimumDistance(string word) {
        int n = word.Length;
        
        var dp = new Dictionary<(int, int), int>();
        dp[(-1, -1)] = 0; // both fingers free
        
        foreach (char ch in word) {
            int cur = ch - 'A';
            var next = new Dictionary<(int, int), int>();
            
            foreach (var kv in dp) {
                int left = kv.Key.Item1;
                int right = kv.Key.Item2;
                int cost = kv.Value;
                
                // move left finger
                var state1 = (cur, right);
                int cost1 = cost + Dist(left, cur);
                if (!next.ContainsKey(state1) || next[state1] > cost1)
                    next[state1] = cost1;
                
                // move right finger
                var state2 = (left, cur);
                int cost2 = cost + Dist(right, cur);
                if (!next.ContainsKey(state2) || next[state2] > cost2)
                    next[state2] = cost2;
            }
            
            dp = next;
        }
        
        int res = int.MaxValue;
        foreach (var v in dp.Values)
            res = Math.Min(res, v);
        
        return res;
    }
}