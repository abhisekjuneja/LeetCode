# Difficulty: Easy
# Problem Statement: https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carryOver, i = 1, len(digits) - 1
        while i > -1 and carryOver > 0:
            carryOver = (digits[i] + 1) // 10
            digits[i] = (digits[i] + 1) % 10
            i -= 1
        return [1] + digits if carryOver else digits