# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        

        while len(lists)>1:
            sortedLists = []
            for i in range(0,len(lists)-1,2):
                head = ListNode()
                tail = head
                while lists[i] and lists[i+1]:
                    if lists[i].val < lists[i+1].val:
                        tail.next = lists[i]
                        lists[i] = lists[i].next
                    else:
                        tail.next = lists[i+1]
                        lists[i+1] = lists[i+1].next
                    tail = tail.next
                
                while lists[i]:
                    tail.next = lists[i]
                    lists[i] = lists[i].next
                    tail = tail.next

                while lists[i+1]:
                    tail.next = lists[i+1]
                    lists[i+1] = lists[i+1].next 
                    tail = tail.next
                
                sortedLists.append(head.next)
            if len(lists) %2 != 0:
                sortedLists.append(lists[-1])
            
            lists= sortedLists
        if not lists: 
            return None
        else:
            return lists[0]           