class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedListAlg:
    def __init__(self):
        self.head = None

    def remove_listnode(self, head, val):
        if head is None:
            return None
        dummy_head = ListNode(next=head)
        cur = dummy_head
        while cur.next is not None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy_head.next

    def inverse_list(self, head):
        if head is None:
            return None
        dummy_head = ListNode(next=head)
        cur = dummy_head
        while cur.next is not None:
            cur.next, cur.next.next, cur = cur.next.next, cur, cur.next
        return dummy_head.next
