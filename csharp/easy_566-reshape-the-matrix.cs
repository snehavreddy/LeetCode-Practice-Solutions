public class Solution {
    public int[][] MatrixReshape(int[][] mat, int r, int c) {
        int rows = mat.Length;
        int cols = mat[0].Length;

        if((rows * cols) != (r * c)) return mat;

        int[][] grid = new int[r][];

        for(int i = 0; i < r; i++)
        {
            grid[i] = new int[c];
        }
        for(int i = 0; i < rows; i++)
        {
            for(int j = 0; j < cols; j++)
            {
                int index = i * cols + j;
                int newRow = index / c;
                int newCol = index % c;

                grid[newRow][newCol] = mat[i][j];                            
            }
        }

        return grid;
    }
}