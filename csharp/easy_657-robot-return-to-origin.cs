public class Solution {
    public bool JudgeCircle(string moves) {
        int leftRight = 0, upDown = 0;

        foreach(char m in moves)
        {
            if(m == 'U') upDown++;
            else if(m == 'D') upDown--;
            else if(m == 'L') leftRight--;
            else if(m == 'R') leftRight++;
        }

        return (leftRight == 0 && upDown == 0);
    }
}