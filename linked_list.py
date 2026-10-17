class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        """Insert a new node at the front of the list. O(1)."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a new node at the end of the list. O(n) to reach the end."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def recursive_sum(self):
        """Return the sum of all node data using recursion."""

        def helper(node):
            # Base case: past the last node, nothing left to add
            if node is None:
                return 0
            # Recursive case: this node's data plus the sum of the rest
            return node.data + helper(node.next)

        return helper(self.head)

    def recursive_reverse(self):
        """Reverse the list in place using recursion."""

        def helper(prev, current):
            # Base case: reached the end, prev is the new head
            if current is None:
                return prev
            # Recursive case: point current back at prev, then move forward
            next_node = current.next
            current.next = prev
            return helper(current, next_node)

        self.head = helper(None, self.head)

    def recursive_search(self, target):
        """Return True if target is in the list, otherwise False, using recursion."""

        def helper(node):
            # Base case: reached the end without finding target
            if node is None:
                return False
            # Base case: found target
            if node.data == target:
                return True
            # Recursive case: keep looking in the rest of the list
            return helper(node.next)

        return helper(self.head)

    def display(self):
        """Print the list as 'val -> val -> val -> None' and return that string."""
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.data))
            current = current.next
        values.append("None")
        output = " -> ".join(values)
        print(output)
        return output
