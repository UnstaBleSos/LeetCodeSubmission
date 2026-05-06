"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        freq={}
        curr = head
        orginial = head
        while head:
            dummy = Node(0)
            dummy.val = head.val
            freq[head]  = dummy
            head = head.next
        
        while curr:
           copy = freq[curr]
           if curr.next:
            copy.next = freq[curr.next]
           else:
            copy.next = None
           if curr.random: 
            copy.random = freq[curr.random]
           else:
            copy.random = None
           curr= curr.next
        
        return freq[orginial] if orginial else None
        
        