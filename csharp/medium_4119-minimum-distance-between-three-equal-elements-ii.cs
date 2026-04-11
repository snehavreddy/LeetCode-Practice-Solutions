public class Solution {
    public int MinimumDistance(int[] nums) {
        var map = new Dictionary<int, List<int>>();

        // Step 1: store indices
        for (int i = 0; i < nums.Length; i++) {
            if (!map.ContainsKey(nums[i]))
                map[nums[i]] = new List<int>();
            map[nums[i]].Add(i);
        }

        int minDist = int.MaxValue;

        // Step 2: check each number
        foreach (var kv in map) {
            var list = kv.Value;

            if (list.Count < 3) continue;

            // Step 3: check consecutive triples
            for (int i = 0; i <= list.Count - 3; i++) {
                int dist = 2 * (list[i + 2] - list[i]);
                minDist = Math.Min(minDist, dist);
            }
        }

        return minDist == int.MaxValue ? -1 : minDist;
    }
}