public class Solution {
    public int RobotSim(int[] commands, int[][] obstacles) {
        // Directions: N, E, S, W
        int[][] dirs = new int[][] {
            new int[]{0,1}, new int[]{1,0},
            new int[]{0,-1}, new int[]{-1,0}
        };

        int dir = 0; // start facing North
        int x = 0, y = 0;
        int maxDist = 0;

        // Store obstacles
        HashSet<string> obs = new HashSet<string>();
        foreach (var o in obstacles) {
            obs.Add(o[0] + "," + o[1]);
        }

        foreach (int cmd in commands) {
            if (cmd == -1) {
                dir = (dir + 1) % 4; // turn right
            } else if (cmd == -2) {
                dir = (dir + 3) % 4; // turn left
            } else {
                for (int i = 0; i < cmd; i++) {
                    int nx = x + dirs[dir][0];
                    int ny = y + dirs[dir][1];

                    if (obs.Contains(nx + "," + ny)) break;

                    x = nx;
                    y = ny;
                    maxDist = Math.Max(maxDist, x*x + y*y);
                }
            }
        }

        return maxDist;
    }
}