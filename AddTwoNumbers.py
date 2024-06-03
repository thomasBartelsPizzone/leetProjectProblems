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
    """
    # not good
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp_ll = ListNode(0)
        last_node = temp_ll
        rem = 0
        while l1 or l2 or rem != 0:
            # print("num1: ", num1)
            # print("num2: ", num2)
            if l1:
                num1 = l1.val
            else:
                num1 = 0
            if l2:
                num2 = l2.val
            else:
                num2 = 0
            
            tot = rem + num1 + num2
            new_node_val = tot % 10
            rem = tot // 10

            if l1:
                l1 = l1.next
            else:
                # num1 = 0
                l1 = None
            if l2:
                l2 = l2.next
            else:
                # num2 = 0
                l2 = None

            new_node = ListNode(new_node_val)
            last_node.next = new_node
            last_node = last_node.next
        
        new_ll = temp_ll.next
        temp_ll.next = None
        return new_ll
    """
    """
    # Works
    def new_linked_list(self, sum_list) -> ListNode:
        rev_list = sum_list[::-1]
        head = None
        for val in rev_list:
            new_node = ListNode(val)
            new_node.next = head
            head = new_node
            # head = new_node
        return head
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem = 0
        # print(l1)
        # print(l2)
        num1 = 0
        # # num1 += ListNode(l1.val * 1)
        num2 = 0
        # if l1:
        #     num1 = l1.val * 1
        # if l2:
        #     num2 = l2.val * 1
        # # num2 += l2.val * 1
        # # # print(num1)
        sol = []
        # while num1 or num2 or rem != 0:
        while l1 or l2 or rem != 0:
            # print("num1: ", num1)
            # print("num2: ", num2)
            if l1:
                num1 = l1.val * 1
            else:
                num1 = 0
            if l2:
                num2 = l2.val * 1
            else:
                num2 = 0
            tot = rem + num1 + num2
            # print("tot: ", tot)
            sol.append(tot % 10)
            # print("sol: ", sol)
            rem = math.trunc(tot/10)
            if l1:
                l1 = l1.next
            else:
                # num1 = 0
                l1 = None
            if l2:
                l2 = l2.next
            else:
                # num2 = 0
                l2 = None
        return self.new_linked_list(sol)
        """

if __name__ == "__main__":
    c = Solution()
    l1 = ListNode(2, ListNode(4, ListNode(3, None)))
    l2 = ListNode(5, ListNode(6, ListNode(4, None)))
    print(c.addTwoNumbers(l1, l2))