class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:
            # Step 1: Check if we have k nodes
            node = prev
            for _ in range(k):
                node = node.next
                if not node:
                    return dummy.next   # fewer than k nodes left → done

            # Step 2: Reverse k nodes
            curr = prev.next
            nxt = curr.next
            for _ in range(k - 1):
                curr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = curr.next

            # Step 3: Move prev to end of this group
            prev = curr
