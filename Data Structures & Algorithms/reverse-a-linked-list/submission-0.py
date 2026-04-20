# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev= None
        currentNode = head
        while currentNode:
            next_node = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = next_node

        return prev
