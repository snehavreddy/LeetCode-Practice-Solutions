public class Solution {
    public void ReverseString(char[] s) {
        int right = s.Length - 1, left = 0;
        while(left < right)
        {
            (s[left], s[right]) = (s[right], s[left]);
            left++;
            right--;
        }
    }
}