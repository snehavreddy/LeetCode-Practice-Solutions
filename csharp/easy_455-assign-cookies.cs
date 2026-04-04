public class Solution {
    public int FindContentChildren(int[] g, int[] s) {
        int g_pointer = 0, s_pointer = 0, gSize = g.Length, sSize = s.Length;
        Array.Sort(g);
        Array.Sort(s);
        while(s_pointer < sSize && g_pointer < gSize)
        {
            if(s[s_pointer] >= g[g_pointer])
            {
                g_pointer++;
            }
            s_pointer++;
        }
        return g_pointer;
    }
}