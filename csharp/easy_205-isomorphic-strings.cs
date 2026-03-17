public class Solution {
    public bool IsIsomorphic(string s, string t) {
        if (s.Length != t.Length) return false;

        Dictionary<char, char> mapST = new Dictionary<char, char>();
        Dictionary<char, char> mapTS = new Dictionary<char, char>();

        for (int i = 0; i < s.Length; i++) {
            char c1 = s[i];
            char c2 = t[i];

            // Check s -> t
            if (mapST.ContainsKey(c1)) {
                if (mapST[c1] != c2) return false;
            } else {
                mapST[c1] = c2;
            }

            // Check t -> s
            if (mapTS.ContainsKey(c2)) {
                if (mapTS[c2] != c1) return false;
            } else {
                mapTS[c2] = c1;
            }
        }

        return true;
    }
}