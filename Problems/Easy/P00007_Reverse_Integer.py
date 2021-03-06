# Problem: https://leetcode.com/problems/reverse-integer/submissions/

class Solution:
    def reverse(self, x: int) -> int:
        xIsNegative = x < 0
        xStrAbs = str(x)[1:] if xIsNegative else str(x)
        xReverseAbs = int(xStrAbs[::-1])
        xReverse = -1 * xReverseAbs if xIsNegative else xReverseAbs
        return xReverse if xReverse in range(-1 * (2 ** 31), 2 ** 31, 1) else 0