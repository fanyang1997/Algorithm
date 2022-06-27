class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedListAlg:
    def __init__(self):
        pass

    # leetcode 203
    def removeElement(self, head, val):
        """
        [1, 2, 3, 4, 5]
        val = 4
        [1, 2, 3, 5]

        :param head:
        :param val:
        :return:
        1-2-3-4-5 val = 4
        0-1-2-3-4-5

        """

        if not head:
            return
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while pre.next:
            if pre.next.val == val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return dummy.next


