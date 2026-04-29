# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

        rh = slow.next
        rcurr = rh
        slow.next = None
        prev = None
        while rcurr:
            node = rcurr.next
            rcurr.next =prev
            prev = rcurr
            rcurr = node
        
        while prev:
            phead = head.next
            head.next = prev
            head = phead
        
            pc = prev.next
            prev.next = phead
            prev = pc
            

        

        





        
        
