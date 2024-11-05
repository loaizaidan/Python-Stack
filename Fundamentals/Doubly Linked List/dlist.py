#  __         ______     ______     __   
# /\ \       /\  __ \   /\  __ \   /\ \  
# \ \ \____  \ \ \/\ \  \ \  __ \  \ \ \ 
#  \ \_____\  \ \_____\  \ \_\ \_\  \ \_\
#   \/_____/   \/_____/   \/_/\/_/   \/_/ 

# Key differences between Singly vs. Doubly Linked Lists
# SLists:

# Each node contains a value and a pointer to the next node.
# Can only be traversed in one direction (from head to tail).
# Simpler implementation and requires less memory.


# DLists:

# Each node contains a value, a pointer to the next node, and a pointer to the previous node.
# Can be traversed in both directions.
# More complex implementation and requires more memory due to the additional pointer.

# Research by Loai Z.

#Implementation: 


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_end(self, val):
        new_node = Node(val)
        if not self.head:  # If the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_node(self, node):
        if not node:
            return
        if node == self.head:
            self.head = node.next
            if self.head:
                self.head.prev = None
        elif node == self.tail:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def insert_after(self, prev_node, val):
        if not prev_node:
            return
        new_node = Node(val)
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next = new_node
        if new_node.next:
            new_node.next.prev = new_node
        else:
            self.tail = new_node  # Update tail if we inserted at the end

    def print_values(self):
        runner = self.head
        while runner:
            print(runner.value, end=" <=> ")
            runner = runner.next
        print("None")

# Testing the Doubly Linked List
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.add_to_end(1)
    dll.add_to_end(2)
    dll.add_to_end(3)
    print("Initial List:")
    dll.print_values()

    dll.insert_after(dll.head, 1.5)
    print("\nAfter inserting 1.5 after 1:")
    dll.print_values()

    dll.delete_node(dll.head.next)  # Deleting node with value 2
    print("\nAfter deleting 2:")
    dll.print_values()

