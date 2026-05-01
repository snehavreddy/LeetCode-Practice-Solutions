public class Solution {
    public int MaxRotateFunction(int[] nums) {
        int n = nums.Length;
        
        long sum = 0;
        long f = 0;
        
        // Step 1: calculate sum and F(0)
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            f += i * nums[i];
        }
        
        long max = f;
        
        // Step 2: use relation
        for (int k = 1; k < n; k++) {
            f = f + sum - (long)n * nums[n - k];
            max = Math.Max(max, f);
        }
        
        return (int)max;
    }
}