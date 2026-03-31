public class Solution {
    public int FindPoisonedDuration(int[] timeSeries, int duration) {
      if (timeSeries.Length == 0) return 0;

    int total = 0;

    for (int i = 0; i < timeSeries.Length - 1; i++)
    {
        int gap = timeSeries[i + 1] - timeSeries[i];
        total += Math.Min(gap, duration);
    }

    return total + duration; // last attack always adds full duration  
    }
}