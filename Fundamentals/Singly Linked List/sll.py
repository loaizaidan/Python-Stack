#  __         ______     ______     __   
# /\ \       /\  __ \   /\  __ \   /\ \  
# \ \ \____  \ \ \/\ \  \ \  __ \  \ \ \ 
#  \ \_____\  \ \_____\  \ \_\ \_\  \ \_\
#   \/_____/   \/_____/   \/_/\/_/   \/_/ 


class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None
    
    def add_to_front(self, val):
        new_node = SLNode(val)
        new_node.next = self.head
        self.head = new_node
        return self

    def print_values(self):
        runner = self.head
        while runner:
            print(runner.value)
            runner = runner.next
        return self

    def add_to_back(self, val):
        if not self.head:
            return self.add_to_front(val)

        runner = self.head
        while runner.next:
            runner = runner.next
        runner.next = SLNode(val)
        return self

    def remove_from_front(self):
        if not self.head:
            return None
        removed_value = self.head.value
        self.head = self.head.next
        return removed_value

    def remove_from_back(self):
        if not self.head:
            return None
        if not self.head.next:
            return self.remove_from_front()

        runner = self.head
        while runner.next.next:
            runner = runner.next
        removed_value = runner.next.value
        runner.next = None
        return removed_value

    def remove_val(self, val):
        if not self.head:
            return None
        if self.head.value == val:
            return self.remove_from_front()

        runner = self.head
        while runner.next:
            if runner.next.value == val:
                removed_value = runner.next.value
                runner.next = runner.next.next
                return removed_value
            runner = runner.next

        return None


my_list = SList()
print("Adding to front and back:")
my_list.add_to_front("2").add_to_front("1").add_to_back("3").print_values()
print("\n")

my_list = SList()
my_list.add_to_back("first").add_to_back("second").add_to_back("third")
print("Initial List:")
my_list.print_values()

print("\nRemove from front:")
my_list.remove_from_front()
print("After removing from front:")
my_list.print_values()

print("\nRemove from back:")
my_list.remove_from_back()
print("After removing from back:")
my_list.print_values()

print("\nRemove value 'second':")
my_list.remove_val("second")
print("After removing 'second':")
my_list.print_values()
