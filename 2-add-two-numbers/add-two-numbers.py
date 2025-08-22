# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        linkedlist=ListNode()
        a=linkedlist
        p=l1
        q=l2
        carry=0
        while p or q or carry:
            x=p.val if p else 0
            y=q.val if q else 0
            total=x+y+carry
            carry=total//10
            a.next=ListNode(total%10)
            a=a.next
            if p:
                p=p.next
            if q:
                q=q.next
        return linkedlist.next