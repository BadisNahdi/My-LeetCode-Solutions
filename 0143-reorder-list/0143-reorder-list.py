# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow
        first = head
        curr, prev = mid, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        second = prev

        while second.next:
            temp1 = first.next
            first.next = second
            first = temp1
            temp2 = second.next
            second.next = first
            second = temp2

        
        