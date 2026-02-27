public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        // Brute force -> n^2
    //     int len = nums.Length;
    //     int[] result = new int[2];
    //     for(int i = 0; i < len; i++)
    //     {
    //         int y = target - nums[i];

    //         for(int j = 0; j < len; j++)
    //         {
    //             if(nums[j] == y)
    //             {
    //                 result[0] = j;
    //                 result[1] = i;
    //                 break;
    //             }
    //         }
    //     }
    //     return result;
    // }

    // Optimal Approach
    Dictionary<int, int> map = new Dictionary<int, int>();

    for(int i = 0; i < nums.Length; i++)
    {
        int num2 = target - nums[i];

        if(map.ContainsKey(num2))
        {
            return new int[] {map[num2], i};
        }else
        {
            map[nums[i]] = i;
        }
    }
       return new int[] {};
    }
}