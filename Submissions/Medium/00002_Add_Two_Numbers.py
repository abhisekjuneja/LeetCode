# Difficulty: Medium
# Problem Statement: https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, L1: ListNode, L2: ListNode) -> ListNode:
        
        H = ListNode(0)
        T = H
        
        C = 0
        while L1 or L2:
            N1 = L1.val if L1 else 0
            N2 = L2.val if L2 else 0
            
            S = N1 + N2 + C
            C = S // 10
            
            T.next = ListNode(S % 10)
            T = T.next
            
            L1 = L1.next if L1 else None
            L2 = L2.next if L2 else None
            
        if C: T.next = ListNode(C)
            
        return H.next