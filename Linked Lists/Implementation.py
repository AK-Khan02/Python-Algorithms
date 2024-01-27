class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """Append a new node with the given value to the end of the list."""
        if not self.head:
            self.head = ListNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(value)

    def display(self):
        """Print out the linked list."""
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        print(" -> ".join(map(str, elements)))
