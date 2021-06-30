# Difficulty: Easy
# Problem Statement: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if not head: return None
        
        previousNode = head
        currentNode = head.next
        
        while currentNode:
            if currentNode.val == previousNode.val:
                previousNode.next = currentNode.next
            else:
                previousNode = currentNode
                
            currentNode = currentNode.next
            
        return head
                