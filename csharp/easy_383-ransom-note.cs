public class Solution {
    public bool CanConstruct(string ransomNote, string magazine) {
        int[] count = new int[26];

        // Count letters in magazine
        foreach (char c in magazine) {
            count[c - 'a']++;
        }

        // Try to build ransomNote
        foreach (char c in ransomNote) {
            if (count[c - 'a'] == 0) {
                return false;
            }
            count[c - 'a']--;
        }

        return true;
    }
}