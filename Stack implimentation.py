'''
class Stack:
    def _init_(self, max_size=None):
        self.items = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        if self.max_size is None:
            return False  # Stack is not full if there is no maximum size
        else:
            return len(self.items) == self.max_size

    def push(self, item):
        if not self.is_full():
            self.items.append(item)
        else:
            raise IndexError("push to a full stack")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def size(self):
        return len(self.items)

# Example usage:
stack = Stack(max_size=3)

print("Is the stack empty?", stack.is_empty())
print("Is the stack full?", stack.is_full())

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:", stack.items)
print("Size of the stack:", stack.size())

print("Is the stack full?", stack.is_full())

# Uncomment the line below to see the exception when trying to push to a full stack
# stack.push(4)
'''

'''
class Stack:
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.max_size

    def push(self, item):
        if not self.is_full():
            self.items.append(item)
        else:
            raise StackFullError("Cannot push to a full stack")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise StackEmptyError("Cannot pop from an empty stack")

    def size(self):
        return len(self.items)


class StackFullError(Exception):
    pass


class StackEmptyError(Exception):
    pass

# Example usage:
stack = Stack(max_size=3)

print("Is the stack empty?", stack.is_empty())
print("Is the stack full?", stack.is_full())

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:", stack.items)
print("Size of the stack:", stack.size())

print("Is the stack full?", stack.is_full())

# Uncomment the line below to see the exception when trying to push to a full stack
# stack.push(4)

'''
# import os

# d_drive_path = "D:\\"

# p1_folder_path = os.path.join(d_drive_path, "Prateek Chaudhary")
# if not os.path.exists(p1_folder_path):
#     os.mkdir(p1_folder_path)

# test_file_path = os.path.join(p1_folder_path, "test.txt")
# with open(test_file_path, "w") as test_file:
#     test_file.write("This is a test file created in the P1 folder.")

# print(f"File 'Content.txt' has been created in the 'P1' folder on the D drive.")




#  ________________________Linked list node_______________________
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next_node
            return

        current_node = self.head
        while current_node.next_node and current_node.next_node.data != data:
            current_node = current_node.next_node

        if current_node.next_node:
            current_node.next_node = current_node.next_node.next_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next_node
        print("None")

# Example usage:
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

linked_list.display()  # Output: 1 -> 2 -> 3 -> None

linked_list.prepend(0)

linked_list.display()  # Output: 0 -> 1 -> 2 -> 3 -> None

linked_list.delete(2)

linked_list.display()  # Output: 0 -> 1 -> 3 -> None
'''

'''
class Node:
    def __init__(self) -> None:
        self.data = data
        self.node_node = None

n1 = Node(13)
n1 = Node(14)
n1 = Node(15)

temp=n1
while temp is not None:
    print(temp.data, '->')
    temp = temp.addr
temp.next_node=n2
'''


'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

n1 = Node(13)
n2 = Node(14)
n3 = Node(15)

# Link the nodes
n1.next_node = n2
n2.next_node = n3

# Print the linked list
temp = n1
while temp is not None:
    print(temp.data, '->', end=' ')
    temp = temp.next_node
print("None")
'''

#linked list 

class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

   def listprint(self):
      printval = self.headval
      while printval is not None:
         print(printval.dataval)
         printval = printval.nextval

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.listprint()