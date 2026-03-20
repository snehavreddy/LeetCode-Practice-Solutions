public class Solution {
    public int[][] FloodFill(int[][] image, int sr, int sc, int color) {
        int original = image[sr][sc];
        
        if (original == color) return image;
        
        DFS(image, sr, sc, original, color);
        return image;
    }

    private void DFS(int[][] image, int r, int c, int original, int color) {
        // boundary check
        if (r < 0 || c < 0 || r >= image.Length || c >= image[0].Length)
            return;

        // stop if not same color
        if (image[r][c] != original)
            return;

        // paint
        image[r][c] = color;

        // explore 4 directions
        DFS(image, r + 1, c, original, color);
        DFS(image, r - 1, c, original, color);
        DFS(image, r, c + 1, original, color);
        DFS(image, r, c - 1, original, color);
    }
}