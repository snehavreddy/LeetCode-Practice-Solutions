public class Solution {
    public int EraseOverlapIntervals(int[][] intervals) {
         if (intervals.Length == 0) return 0;

        int size = intervals.Length;
        // Sort based on end
        Array.Sort(intervals, (a,b) => a[1].CompareTo(b[1]));
        int count = 1, prevEnd = intervals[0][1];
        for(int i = 1; i < size; i++)
        {
            // Non - Overlapping intervals
            if(intervals[i][0] >= prevEnd)
            {
                count++;
                prevEnd = intervals[i][1];
            }
        }
        return size - count;
    }
}