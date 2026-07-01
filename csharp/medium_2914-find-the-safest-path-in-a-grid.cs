public class Solution {
    public int MaximumSafenessFactor(IList<IList<int>> grid) {
        int n = grid.Count;
        int[][] dist = new int[n][];
        for (int i = 0; i < n; i++) {
            dist[i] = new int[n];
            Array.Fill(dist[i], -1);
        }

        // 1. Multi-source BFS to calculate distance to the nearest thief
        Queue<(int, int)> queue = new Queue<(int, int)>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    dist[i][j] = 0;
                    queue.Enqueue((i, j));
                }
            }
        }

        int[][] dirs = new int[][] { new int[] { 0, 1 }, new int[] { 0, -1 }, new int[] { 1, 0 }, new int[] { -1, 0 } };

        while (queue.Count > 0) {
            var (r, c) = queue.Dequeue();
            foreach (var d in dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && dist[nr][nc] == -1) {
                    dist[nr][nc] = dist[r][c] + 1;
                    queue.Enqueue((nr, nc));
                }
            }
        }

        // 2. Modified Dijkstra using PriorityQueue (Max-Heap)
        // C# PriorityQueue is a Min-Heap by default, so use negative values for Max-Heap
        PriorityQueue<(int, int), int> pq = new PriorityQueue<(int, int), int>(Comparer<int>.Create((a, b) => b.CompareTo(a)));
        
        pq.Enqueue((0, 0), dist[0][0]);
        dist[0][0] = -1; // Mark as visited

        while (pq.Count > 0) {
            pq.TryDequeue(out var curr, out int safety);
            int r = curr.Item1, c = curr.Item2;

            if (r == n - 1 && c == n - 1) return safety;

            foreach (var d in dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && dist[nr][nc] != -1) {
                    int newSafety = Math.Min(safety, dist[nr][nc]);
                    pq.Enqueue((nr, nc), newSafety);
                    dist[nr][nc] = -1; // Mark as visited
                }
            }
        }

        return 0;
    }
}