class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(n: int) -> int:
            if n < 100: return 0
            s = str(n)
            memo = {}

            def dp(pos, is_less, is_started, last, prev_last, count):
                state = (pos, is_less, is_started, last, prev_last, count)
                if state in memo: return memo[state]
                
                if pos == len(s):
                    return count
                
                res = 0
                upper = int(s[pos]) if not is_less else 9
                
                for digit in range(upper + 1):
                    new_is_less = is_less or (digit < upper)
                    
                    if not is_started:
                        if digit == 0:
                            res += dp(pos + 1, new_is_less, False, -1, -1, 0)
                        else:
                            res += dp(pos + 1, new_is_less, True, digit, -1, 0)
                    else:
                        # Determine if 'last' is a peak or valley
                        new_waviness = 0
                        if prev_last != -1:
                            if (prev_last < last > digit) or (prev_last > last < digit):
                                new_waviness = 1
                        
                        res += dp(pos + 1, new_is_less, True, digit, last, count + new_waviness)
                
                memo[state] = res
                return res

            return dp(0, False, False, -1, -1, 0)

        return solve(num2) - solve(num1 - 1)