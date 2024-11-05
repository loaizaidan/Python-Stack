#  __         ______     ______     __   
# /\ \       /\  __ \   /\  __ \   /\ \  
# \ \ \____  \ \ \/\ \  \ \  __ \  \ \ \ 
#  \ \_____\  \ \_____\  \ \_\ \_\  \ \_\
#   \/_____/   \/_____/   \/_/\/_/   \/_/ 
                                       
class Is


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Stack:
    class Node:
        def __init__(self, element, next):
            self.element = element
            self.next = next

    def __init__(self):
        self.head = None
        self.size = 0            

    def __len__(self):
        return self.size

    def is_empty(self):
         return self.size == 0

    def push(self, element):
        self.head = self.Node(element, self.head)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise isEmptyError('This stack is emoty, therefore cannot pop.')
    
def getLen(head):
    len = 0
    while head:
        len +=1
        head = head.next
    return len

def getNode(head):
    for i in range(0,2,1):
        print("ttt",head.value)
        head = head.next

v1 = Node("1")
v2 = Node("2")
v3 = Node("3")
v4 = Node("4")
v5 = Node("5")

v1.next = v2
v2.next = v3
v3.next = v4
v4.next = v5

mainval = v1

# print(v1.value)
# print(v2.value)
# print("\n")
# print(getLen(mainval))
# print("\n")
# getNode(mainval)
# print("\n")

# while mainval is not None:
#     print(mainval.value)
#     mainval = mainval.next

# print("\n")
# new_node = Node(0)
# new_node.next = v1

# mainval = new_node
# while mainval is not None:
#     print(mainval.value)
#     mainval = mainval.next

# print("\n")

# new_tail = Node(6)
# head = new_node

# while head.next is not None:
#     head = head.next

# head.next = new_tail
# mainval = new_node

# while mainval is not None:
#     print(mainval.value)
#     mainval = mainval.next

# print("\n")
# new_node= Node(100)
# pointer = v1
# pos = 3
# for i in range(1,pos -1):
#     pointer = pointer.next
# new_node.next = pointer.next
# pointer.next = new_node



# temp = mainval
# mainval = mainval.next
# del temp

# current = mainval

# while current and current.next and current.next.next:
#     current = current.next

# if current and current.next:
#     print

# while mainval is not None:
#     print(mainval.value)
#     mainval = mainval.next