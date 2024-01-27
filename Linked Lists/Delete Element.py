def delete(self, value):
    """Delete the first occurrence of the value in the list."""
    current = self.head
    if current is None:
        return

    if current.value == value:
        self.head = current.next
        return

    while current.next:
        if current.next.value == value:
            current.next = current.next.next
            return
        current = current.next
