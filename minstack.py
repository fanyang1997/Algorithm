
# eg. MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

class MinStack:
    def __init__(self):
        self.A = []
        self.B = []

    def push(self, x: int) -> None:
        self.A.append(x)
        if not self.B or x <= self.B[-1]:
            self.B.append(x)

    def pop(self):
        if self.A.pop() == self.B[-1]:
            self.B.pop()

    def top(self):
        return self.A[-1]

    def min(self):
        return self.B[-1]


class CQueue:
    def __init__(self):
        self.A = []
        self.B = []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if not self.A:
            return -1
        if not self.B:
            while self.A:
                self.B.append(self.A.pop())
        return self.B.pop()

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    return prev

def findTheDifference(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    s_dict = {}
    for c in s:
        if c in s_dict:
            s_dict[c] += 1
        else:
            s_dict[c] = 1

    for c in t:
        if c not in s_dict or s_dict[c] == 0:
            return c
        else:
            s_dict[c] -= 1


if __name__ == "__main__":
    s = 'abcd'
    t = 'abcde'
    print(findTheDifference(s, t))