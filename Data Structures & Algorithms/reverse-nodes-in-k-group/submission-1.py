# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        dummy= ListNode(0,head)
        prevgroup = dummy
        node = prevgroup
        while True:
            for i in range(k):
                if not node:
                    return dummy.next
                node = node.next
            
            if not node:
                return dummy.next
            nextgroup = node.next

            prev = nextgroup
            curr = prevgroup.next
            oldhead = prevgroup.next
            for i in range(k):
                current = curr.next
                curr.next = prev
                prev = curr
                curr = current
            
            prevgroup.next = prev
            prevgroup = oldhead
            node = prevgroup
        
        return dummy.next
            

            
            
            

                

            
