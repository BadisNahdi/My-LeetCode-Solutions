class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        prev = head
        curr = head.next

        first = -1
        prev_critical = -1

        min_dis = float('inf')
        max_dis = 0

        pos = 1

        while curr.next:
            if ((prev.val < curr.val and curr.val > curr.next.val) or
                (prev.val > curr.val and curr.val < curr.next.val)):

                if first == -1:
                    first = pos
                else:
                    min_dis = min(min_dis, pos - prev_critical)

                    max_dis = pos - first

                prev_critical = pos

            prev = curr
            curr = curr.next
            pos += 1

        if first == -1 or first == prev_critical:
            return [-1, -1]

        return [min_dis, max_dis]