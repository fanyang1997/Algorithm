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

    def swap_pairs(self, head):
        if head is None or head.next is None:
            return head
        dummy_head = ListNode(next=head)
        cur = dummy_head
        while cur.next is not None and cur.next.next is not None:
            cur.next, cur.next.next, cur.next.next.next, cur = cur.next.next, cur, cur.next.next.next, cur.next.next
        return dummy_head.next

    def remove_nth_from_end(self, head, n):
        if head is None:
            return None
        dummy_head = ListNode(next=head)
        cur = dummy_head
        while cur.next is not None:
            if n == 0:
                cur.next = cur.next.next
            else:
                cur = cur.next
                n -= 1
        return dummy_head.next

    def get_intersection_node(self, headA, headB):

        if headA is None or headB is None:
            return None
        lenA = 0
        lenB = 0
        curA = headA
        curB = headB
        while curA is not None:
            lenA += 1
            curA = curA.next
        while curB is not None:
            lenB += 1
            curB = curB.next
        if lenA > lenB:
            for i in range(lenA - lenB):
                headA = headA.next
        else:
            for i in range(lenB - lenA):
                headB = headB.next
        while headA is not None and headB is not None:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

