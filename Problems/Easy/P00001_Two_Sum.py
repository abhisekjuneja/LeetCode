# Problem: https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Create a Dictionary for the Numbers and their Count in the List
        D = {}
        for n in nums:
            D[n] = D.get(n, 0) + 1
            
        # Iterate over the List and Find Pairs of Numbers
        N = []
        for na in nums:
            nb = target - na
            if na == nb and D.get(na, 0) == 2:
                N = [na, nb]
                break
                
            elif na != nb and D.get(nb, 0) > 0:
                N = [na, nb]
                break
                
        # Find the Index of the Number Pair
        i = nums.index(N[0])
        j = nums.index(N[0], i + 1) if N[0] == N[1] else nums.index(N[1])
        
        return [i, j]