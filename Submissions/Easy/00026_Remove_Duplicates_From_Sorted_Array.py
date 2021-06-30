# Difficulty: Easy
# Problem Statement: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        previousNumber, i = float('inf'), 0
        
        while i < len(nums):
            if nums[i] == previousNumber:
                del nums[i]
            else:
                previousNumber = nums[i]
                i += 1