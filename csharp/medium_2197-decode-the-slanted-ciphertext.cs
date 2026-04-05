public class Solution {
    public string DecodeCiphertext(string encodedText, int rows) {
        if(rows == 0) return "";
        if(rows == 1) return encodedText;

        // find columns
        int size = encodedText.Length;
        int cols = size / rows;
        
        // Prepare a matrix
        char[,] matrix = new char[rows,cols];
        int index = 0;
        for(int i = 0; i < rows; i++)
        {
            for(int j = 0; j < cols; j++)
            {
                matrix[i, j] = encodedText[index++];
            }
        }
        // Read characters diagonally and append to string
        StringBuilder original = new StringBuilder();
        for(int k = 0; k < cols; k++)
        {
            int i = 0, j = k; // rows starts from 0 , col will increment by 1 for each iteration
            while(i < rows && j < cols)
            {
                original.Append(matrix[i, j]);
                i++;
                j++;
            }
        }
        return original.ToString().TrimEnd();
    }
}