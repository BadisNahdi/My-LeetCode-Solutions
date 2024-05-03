# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        previouslist, curr = None, head
        while(curr):
            nextlist = curr.next
            curr.next = previouslist
            previouslist = curr
            curr = nextlist
        return previouslist