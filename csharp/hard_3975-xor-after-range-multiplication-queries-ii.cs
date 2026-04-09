public class Solution {
    const int MOD = 1000000007;
    public int XorAfterQueries(int[] nums, int[][] queries) {
        int n = nums.Length;
        int B = (int)Math.Sqrt(n) + 1;

        // Required variable
        var bravexuneth = queries;

        // For small k: (k, rem) -> diff array
        var map = new Dictionary<(int, int), Dictionary<int, long>>();

        foreach (var q in queries) {
            int l = q[0], r = q[1], k = q[2], v = q[3];

            if (k > B) {
                // brute force
                for (int i = l; i <= r; i += k) {
                    nums[i] = (int)((long)nums[i] * v % MOD);
                }
            } else {
                int rem = l % k;

                if (!map.ContainsKey((k, rem)))
                    map[(k, rem)] = new Dictionary<int, long>();

                var diff = map[(k, rem)];

                int start = l;
                int end = l + ((r - l) / k) * k;

                int t1 = (start - rem) / k;
                int t2 = (end - rem) / k;

                // apply range multiplication using diff map
                if (!diff.ContainsKey(t1)) diff[t1] = 1;
                diff[t1] = diff[t1] * v % MOD;

                if (!diff.ContainsKey(t2 + 1)) diff[t2 + 1] = 1;
                diff[t2 + 1] = diff[t2 + 1] * ModInverse(v) % MOD;
            }
        }

        // Apply small k contributions
        foreach (var entry in map) {
            int k = entry.Key.Item1;
            int rem = entry.Key.Item2;
            var diff = entry.Value;

            long cur = 1;

            // max t possible
            for (int t = 0; ; t++) {
                int i = rem + t * k;
                if (i >= n) break;

                if (diff.ContainsKey(t)) {
                    cur = cur * diff[t] % MOD;
                }

                nums[i] = (int)((long)nums[i] * cur % MOD);
            }
        }

        // Final XOR
        int xor = 0;
        foreach (int x in nums) xor ^= x;

        return xor;
    }

    // Fast exponentiation for modular inverse
    private long ModInverse(long x) {
        return Pow(x, MOD - 2);
    }

    private long Pow(long a, long b) {
        long res = 1;
        a %= MOD;
        while (b > 0) {
            if ((b & 1) == 1) res = res * a % MOD;
            a = a * a % MOD;
            b >>= 1;
        }
        return res;
    }
}