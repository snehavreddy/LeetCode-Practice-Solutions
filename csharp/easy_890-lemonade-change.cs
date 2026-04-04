public class Solution {
    public bool LemonadeChange(int[] bills) {
        int five = 0, ten = 0;
        for(int i = 0; i < bills.Length; i++)
        {
            if(bills[i] == 5)
            {
                five++;
            } else if(bills[i] == 10)
            {
               if(five > 0)
               {
                 five --;
                 ten ++;
               }else
               {
                 return false;
               }

            }else if(bills[i] == 20)
            {
                if(ten > 0 && five > 0)
                {
                    ten --;
                    five--;
                }else if(five >= 3)
                {
                    five = five - 3;
                }else {
                    return false;
                }
            }
        }

        return true;
    }
}