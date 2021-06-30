# Difficulty: Easy
# Problem Statement: https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0

        while i < len(nums):
            if target <= nums[i]:
                break
            i += 1
            
        return i