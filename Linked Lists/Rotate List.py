# This algorithm rotates the list to the right by k places, which is a common operation for circular lists or when dealing with buffers.

def rotate_right(head, k):
    if not head or not head.next or k == 0:
        return head

    # Close the linked list into a ring
    old_tail = head
    n = 1
    while old_tail.next:
        old_tail = old_tail.next
        n += 1
    old_tail.next = head

    # Find the new tail : (n - k % n - 1)th node
    # and the new head : (n - k % n)th node
    new_tail = head
    for _ in range(n - k % n - 1):
        new_tail = new_tail.next
    new_head = new_tail.next

    # Break the ring
    new_tail.next = None

    return new_head
