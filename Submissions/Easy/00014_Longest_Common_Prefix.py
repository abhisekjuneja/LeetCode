# Difficulty: Easy
# Problem Statement: https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) < 1:
            return ''
        
        maxStringLength = max([len(S) for S in strs])
        
        i = 0
        while i < maxStringLength and len(set([S[:i + 1] for S in strs])) == 1:
            i += 1
            
        return strs[0][:i]