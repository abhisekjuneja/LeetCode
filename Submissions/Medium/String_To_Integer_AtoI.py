# Difficulty: Medium
# Problem Statement: https://leetcode.com/problems/string-to-integer-atoi

from re import findall

class Solution:
    def myAtoi(self, s: str) -> int:
        
        # Search for Numbers based on the Constraints
        M = findall('^\s*[-+]?\d+', s)
        
        # If no Numbers are Found, Return 0
        if len(M) == 0: return 0
        
        # Otherwise, the First Item in the List, is the Number
        S = M[0]
        
        # Check if the Number contains a Prefixed Sign
        containsSign = S[0] in ('+', '-')
        
        # If the Number Contains One, Store the Sign
        sign = S[0] if containsSign else '+'
        
        # If the Number is Prefixed with a Sign,
        # Then Strip the Number off the Sign
        S = S[1:] if containsSign else S
        
        # Convert the String to an Integer
        N = int(S)
        
        # If the Number was Prefixed with a Negative Sign (-)
        # Then, Multiply the Resulting Number with -1
        N *= -1 if containsSign and sign is '-' else 1
        
        # Limit the Number within the 32 Bit Integer Space
        N = max(min(N, 2 ** 31 - 1), -2 ** 31)
            
        # Return the Number
        return N