class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        #take last item of list and make it the head
        if node is None:
            return None
        #set last node in list to head
        if node.next_node is None:
            self.head = node
            #set new head.next to variable prev
            node.next_node = prev
            return
        #variable for node next to new head
        next_to_head = node.next_node
        #set that variable to prev
        node.next_node = prev
        #recurse
        self.reverse_list(next_to_head, node)
