public class Solution {
    public bool HasValidPath(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;

        // Directions mapping
        var directions = new Dictionary<int, int[][]>() {
            {1, new int[][] { new int[]{0, -1}, new int[]{0, 1} }},
            {2, new int[][] { new int[]{-1, 0}, new int[]{1, 0} }},
            {3, new int[][] { new int[]{0, -1}, new int[]{1, 0} }},
            {4, new int[][] { new int[]{0, 1}, new int[]{1, 0} }},
            {5, new int[][] { new int[]{0, -1}, new int[]{-1, 0} }},
            {6, new int[][] { new int[]{0, 1}, new int[]{-1, 0} }}
        };

        var queue = new Queue<(int, int)>();
        var visited = new HashSet<(int, int)>();

        queue.Enqueue((0, 0));
        visited.Add((0, 0));

        while (queue.Count > 0) {
            var (r, c) = queue.Dequeue();

            if (r == m - 1 && c == n - 1)
                return true;

            foreach (var dir in directions[grid[r][c]]) {
                int nr = r + dir[0];
                int nc = c + dir[1];

                if (nr >= 0 && nr < m && nc >= 0 && nc < n &&
                    !visited.Contains((nr, nc))) {

                    // Check reverse connection
                    foreach (var back in directions[grid[nr][nc]]) {
                        if (back[0] == -dir[0] && back[1] == -dir[1]) {
                            visited.Add((nr, nc));
                            queue.Enqueue((nr, nc));
                            break;
                        }
                    }
                }
            }
        }

        return false;
    }
}