public class Solution {
    public int ClosestTarget(string[] words, string target, int startIndex) {
        int n = words.Length;
        int minDist = int.MaxValue;

        for (int i = 0; i < n; i++) {
            if (words[i] == target) {
                int direct = Math.Abs(i - startIndex);
                int circular = n - direct;
                int dist = Math.Min(direct, circular);
                
                minDist = Math.Min(minDist, dist);
            }
        }

        return minDist == int.MaxValue ? -1 : minDist;
    }
}