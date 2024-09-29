from typing import Optional, List


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        new_l = []
        ctr = 0
        while head:
            new_l.append(head.val)
            head = head.next
            ctr += 1
        print(ctr)
        if ctr == 1:
            return head

        return self.new_linked_list(new_l, n)

    def new_linked_list(self, a: List[int], n: int) -> ListNode:
        m = len(a)
        if m < 2:
            head = ListNode(None)
            head.next = None
            return head
        print(a)
        print(a[-n])
        print(a[-n + 1:])
        # print(a)
        # aa = a
        a = a[:-n] + a[-n + 1:]
        head = ListNode(a[0])
        print(a)
        # print(a)
        tail = head
        for val in a[1:]:
            new_node = ListNode(val)
            tail.next = new_node
            tail = new_node
        return head

if __name__ == "__main__":
    c = Solution()
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    l2 = ListNode(1, None)
    l3 = ListNode(1, ListNode(5, None))
    # print(c.removeNthFromEnd(l1, 2))
    # print(c.removeNthFromEnd(l2, 1))
    print(c.removeNthFromEnd(l3, 1))