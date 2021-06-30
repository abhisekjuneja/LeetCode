# Difficulty: Easy
# Problem Statement: https://leetcode.com/problems/length-of-last-word/

from re import findall

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = findall('\w+', s)
        return 0 if len(words) == 0 else len(words[-1])