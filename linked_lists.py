import sys


class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def print_linked_list(head):
    while head:
        sys.stdout.write(str(head.data))
        sys.stdout.write(" -> ")
        head = head.next
    sys.stdout.write("\n")


def remove_kth_node(head, k):
    """ Removing the kth last element """
    # Using the runner technique
    tom = jerry = head
    for _ in range(k):
        jerry = jerry.next
    while jerry.next:
        tom, jerry = tom.next, jerry.next
    tom.next = tom.next.next
    return head


if __name__ == "__main__":
    head = ListNode(52, None)
    head.next = ListNode(3, None)
    new = head.next.next = ListNode(8)
    new.next = ListNode(15)
    new.next.next = ListNode(2)
    new.next.next.next = ListNode(4)
    print_linked_list(head)
    print_linked_list(remove_kth_node(head, 4))
