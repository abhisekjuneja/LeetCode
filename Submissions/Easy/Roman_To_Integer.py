# Difficulty: Easy
# Problem Statement: https://leetcode.com/problems/roman-to-integer

from re import sub, findall

class Solution:
    def romanToInt(self, S: str) -> int:
        
        # ------------- #
        # SPECIAL CASES #
        # ------------- #
        
        # I can be placed before V (5) and X (10) to make 4 and 9
        S = sub('IX', '(9)', sub('IV', '(4)', S))
        
        # X can be placed before L (50) and C (100) to make 40 and 90. 
        S = sub('XC', '(90)', sub('XL', '(40)', S))
        
        # C can be placed before D (500) and M (1000) to make 400 and 900.
        S = sub('CM', '(900)', sub('CD', '(400)', S))
        
        # ------------- #
        # GENERAL CASES #
        # ------------- #
        
        # SYMBOL: I | VALUE: 1
        S = sub('I', '(1)', S)
        
        # SYMBOL: V | VALUE: 5
        S = sub('V', '(5)', S)
        
        # SYMBOL: X | VALUE: 10
        S = sub('X', '(10)', S)
        
        # SYMBOL: L | VALUE: 50
        S = sub('L', '(50)', S)
        
        # SYMBOL: C | VALUE: 100
        S = sub('C', '(100)', S)
        
        # SYMBOL: D | VALUE: 500
        S = sub('D', '(500)', S)
        
        # SYMBOL: M | VALUE: 1000
        S = sub('M', '(1000)', S)
        
        return sum([int(N) for N in findall('\d+', S)])