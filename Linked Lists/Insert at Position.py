def insert_at_position(self, value, position):
        new_node = ListNode(value)

        if position < 1:
            print("Position should be >= 1.")
            return

        if position == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for i in range(1, position - 1):
                if temp is not None:
                    temp = temp.next
                else:
                    print("The position is greater than the length of the LinkedList.")
                    return

            if temp is None:
                print("The previous node is null.")
            else:
                new_node.next = temp.next
                temp.next = new_node
