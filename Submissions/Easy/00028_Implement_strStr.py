# Difficulty: Easy
# Problem Statement: https://leetcode.com/problems/implement-strstr/

from re import search, compile

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        S = search(compile(needle), haystack)
        return S.start() if S else -1