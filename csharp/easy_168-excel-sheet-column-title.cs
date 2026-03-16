public class Solution {
    public string ConvertToTitle(int columnNumber) {
        string result = "";

        while(columnNumber > 0)
        {
            columnNumber--; 
            int rem = columnNumber % 26;

            char ch = (char)('A' + rem);
            result = ch + result;

            columnNumber /= 26;
        }

        return result;
    }
}