def find(self, value):
    """Returns True if the value is in the list, False otherwise."""
    current = self.head
    while current:
        if current.value == value:
            return True
        current = current.next
    return False
