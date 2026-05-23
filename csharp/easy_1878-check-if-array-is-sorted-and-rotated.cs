public class Solution {
    public bool Check(int[] nums) {
        int count = 0;
        int n = nums.Length;
        
        for (int i = 0; i < n; i++) {
            // Check if the current element is greater than the next element
            // (i + 1) % n handles the wrap-around to compare the last and first element
            if (nums[i] > nums[(i + 1) % n]) {
                count++;
            }
        }
        
        // A sorted and rotated array will have at most 1 point of decrease
        return count <= 1;
    }
}