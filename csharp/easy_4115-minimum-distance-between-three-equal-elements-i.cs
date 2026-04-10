public class Solution {
    public int MinimumDistance(int[] nums) {
        // Map: number → list of indices
        Dictionary<int, List<int>> map = new Dictionary<int, List<int>>();
        
        for (int i = 0; i < nums.Length; i++) {
            if (!map.ContainsKey(nums[i]))
                map[nums[i]] = new List<int>();
            map[nums[i]].Add(i);
        }

        int minDist = int.MaxValue;

        // Check each number
        foreach (var kv in map) {
            var list = kv.Value;

            // Need at least 3 occurrences
            if (list.Count < 3) continue;

            // Try consecutive triples
            for (int i = 0; i <= list.Count - 3; i++) {
                int first = list[i];
                int last = list[i + 2];

                int dist = 2 * (last - first);
                minDist = Math.Min(minDist, dist);
            }
        }

        return minDist == int.MaxValue ? -1 : minDist;
    }
}