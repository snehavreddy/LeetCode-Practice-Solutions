public class Solution {
    public int MatchPlayersAndTrainers(int[] players, int[] trainers) {
        Array.Sort(players);
        Array.Sort(trainers);
        int p_count = 0, t_count = 0;

        while(p_count < players.Length && t_count < trainers.Length)
        {
            if(players[p_count] <= trainers[t_count])
            {
                p_count++;
            }
            t_count++;
        }
        return p_count;
    }
}