def merge_sorted_lists(list1, list2):
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.value < list2.value:
            tail.next, list1 = list1, list1.next
        else:
            tail.next, list2 = list2, list2.next
        tail = tail.next

    tail.next = list1 or list2
    return dummy.next
