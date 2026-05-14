# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # hashset = set()
        # while head:
        #     if head in hashset:
        #         return True
        #     hashset.add(head)
        #     head = head.next
        # return False

        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False