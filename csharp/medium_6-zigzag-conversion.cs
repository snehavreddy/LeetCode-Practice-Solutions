public class Solution {
    public string Convert(string s, int numRows) {
        if (numRows == 1 || s.Length <= numRows)
            return s;

        // Create rows
        var rows = new List<string>();
        for (int i = 0; i < numRows; i++)
            rows.Add("");

        int curRow = 0;
        bool goingDown = false;

        foreach (char c in s) {
            rows[curRow] += c;

            // Flip direction at top or bottom
            if (curRow == 0 || curRow == numRows - 1)
                goingDown = !goingDown;

            curRow += goingDown ? 1 : -1;
        }

        // Combine rows
        return string.Concat(rows);
    }
}