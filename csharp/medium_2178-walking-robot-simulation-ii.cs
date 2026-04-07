public class Robot {

    int width, height;
    int x = 0, y = 0;
    int dir = 0; // 0=East, 1=North, 2=West, 3=South

    int[][] dirs = new int[][] {
        new int[]{1, 0},   // East
        new int[]{0, 1},   // North
        new int[]{-1, 0},  // West
        new int[]{0, -1}   // South
    };

    string[] dirNames = new string[] {"East", "North", "West", "South"};

    int cycle;

    public Robot(int width, int height) {
        this.width = width;
        this.height = height;
        cycle = 2 * (width + height - 2);
    }
    
    public void Step(int num) {
        num = num % cycle;

        // Special case: if full cycle → face South at (0,0)
        if (num == 0) {
            if (x == 0 && y == 0) dir = 3;
            return;
        }

        while (num > 0) {
            int nx = x + dirs[dir][0];
            int ny = y + dirs[dir][1];

            // If out of bounds - turn
            if (nx < 0 || nx >= width || ny < 0 || ny >= height) {
                dir = (dir + 1) % 4;
                continue;
            }

            // Move
            x = nx;
            y = ny;
            num--;
        }
    }
    
    public int[] GetPos() {
        return new int[]{x, y};
    }
    
    public string GetDir() {
        return dirNames[dir];
    }
}