# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and l2:
            return False
        
        carry =0
        arr=[]
        while l1 and l2:
            if carry == 1:
                l1.val = l1.val+carry
            
            digit = (l1.val+l2.val)%10
            carry = (l1.val+l2.val)//10

            arr.append(digit)

            l1=l1.next
            l2= l2.next
        
        while l1 :
           digit = (l1.val+carry)%10
           carry = (l1.val+carry)//10
           arr.append(digit)
           l1=l1.next
        
        while l2:
            digit= (l2.val+carry)%10
            carry = (l2.val+carry)//10
            arr.append(digit)
            l2=l2.next

        head = ListNode(arr[0])
        current = head
        for i in range(1,len(arr)):
            current.next = ListNode(arr[i])
            current = current.next

        if carry:
            current.next = ListNode(carry)
            current = current.next
            

        return head 
            
        
            
           

            
