import sys


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def display_linked_list(head):
    while head:
        sys.stdout.write(str(head.val))
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

def remove_duplicates_with_buffer(head):
    """ Removes duplicates from unsorted linked lists"""
    existing = {}
    previous = ListNode(None)
    current = head
    while current != None:
        if current.val in existing:
            previous.next = current.next
        else:
            existing[current.val] = True
            previous = current
        current = current.next
    return head


def remove_duplicates_without_buffer(head):
    current = head
    while current.next != None:  # Upto the second last node
        print current.val
        runner = current
        while runner.next != None:
            if runner.next.val == current.val:  # Duplicate
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    return head



if __name__ == "__main__":
    head = ListNode(52, None)
    head.next = ListNode(3, None)
    new = head.next.next = ListNode(8)
    new.next = ListNode(15)
    new.next.next = ListNode(2)
    new.next.next.next = ListNode(3)
    # 52 > 3 > 8 > 15 > 2 > 3
    #display_linked_list(head)
    #display_linked_list(remove_kth_node(head, 4))
    display_linked_list(remove_duplicates_without_buffer(head))
