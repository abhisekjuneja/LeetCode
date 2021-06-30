# Difficulty: Easy
# Problem Statement: https://leetcode.com/problems/reverse-linked-list-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        A = []
        while head:
            A += [head.val]
            head = head.next
        
        A = A[:left-1] + A[left-1:right][::-1] + A[right:]
        
        H = ListNode(A[0])
        I = H
        for E in A[1:]:
            N = ListNode(E)
            I.next = N
            I = I.next
        
        return H