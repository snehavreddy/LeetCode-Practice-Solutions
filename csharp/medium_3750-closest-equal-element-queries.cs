public class Solution {
    public IList<int> SolveQueries(int[] nums, int[] queries) {
        int n = nums.Length;
        Dictionary<int, List<int>> map = new Dictionary<int, List<int>>();
        
        for (int i = 0; i < n; i++) {
            if (!map.ContainsKey(nums[i])) {
                map[nums[i]] = new List<int>();
            }
            map[nums[i]].Add(i);
        }
        
        int[] result = new int[queries.Length];
        
        for (int i = 0; i < queries.Length; i++) {
            int targetIdx = queries[i];
            int val = nums[targetIdx];
            List<int> indices = map[val];
            
            if (indices.Count <= 1) {
                result[i] = -1;
                continue;
            }
            
            int pos = indices.BinarySearch(targetIdx);
            
            int prevIdx = (pos == 0) ? indices[indices.Count - 1] : indices[pos - 1];
            int nextIdx = (pos == indices.Count - 1) ? indices[0] : indices[pos + 1];
            
            result[i] = Math.Min(GetDist(targetIdx, prevIdx, n), GetDist(targetIdx, nextIdx, n));
        }
        
        return result;
    }
    
    private int GetDist(int i, int j, int n) {
        int diff = Math.Abs(i - j);
        return Math.Min(diff, n - diff);
    }
}