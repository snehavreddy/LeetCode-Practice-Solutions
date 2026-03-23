public class Solution {
    public bool WordPattern(string pattern, string s) {
        string[] words = s.Split(' ');

        if (pattern.Length != words.Length)
            return false;

        Dictionary<char, string> map1 = new Dictionary<char, string>();
        Dictionary<string, char> map2 = new Dictionary<string, char>();

        for (int i = 0; i < pattern.Length; i++) {
            char ch = pattern[i];
            string word = words[i];

            // Check char -> word
            if (map1.ContainsKey(ch)) {
                if (map1[ch] != word)
                    return false;
            } else {
                map1[ch] = word;
            }

            // Check word -> char
            if (map2.ContainsKey(word)) {
                if (map2[word] != ch)
                    return false;
            } else {
                map2[word] = ch;
            }
        }

        return true;
    }
}