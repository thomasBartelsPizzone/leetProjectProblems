# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    # Works better
    def integerer(self, ll):
        new_int = 0
        ctr = 0
        while ll:
            new_int += (ll.val * 1) * 10**ctr
            # print("new int: ", new_int)
            ll = ll.next
            ctr += 1
        print("new_int: ", new_int)
        return new_int

    def new_linked_list(self, sum_) -> ListNode:
        head = None
        for val in str(sum_):
            # new_node = ListNode(int(val))
            # new_node = ListNode(2, ListNode(4, ListNode(3, None)))
            # new_node = ListNode(int(val))
            new_node = ListNode(val)
            new_node.next = head
            head = new_node
            # head = new_node

        return head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # sum_l1 = summer(l1)
        # sum_l2 = summer(l2)
        # ll_tot = summer(l1) + summer(l2)
        ll_tot = self.integerer(l1) + self.integerer(l2)
        print("ll_tot: ", ll_tot)
        # print(self.new_linked_list(ll_tot))
        return self.new_linked_list(ll_tot)


if __name__ == "__main__":
    c = Solution()
    l1 = ListNode(2, ListNode(4, ListNode(3, None)))
    l2 = ListNode(5, ListNode(6, ListNode(4, None)))
    print(c.addTwoNumbers(l1, l2))