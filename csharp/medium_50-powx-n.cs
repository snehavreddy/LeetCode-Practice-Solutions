public class Solution {
    public double MyPow(double x, int n) {
        long N = n; // handle overflow
        
        if (N < 0) {
            x = 1 / x;
            N = -N;
        }
        
        double result = 1;
        
        while (N > 0) {
            if (N % 2 == 1) {   // odd
                result *= x;
            }
            
            x *= x;   // square
            N /= 2;   // reduce power
        }
        
        return result;
    }
}