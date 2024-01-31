# the first thing is to divide the list into two parts
#first node
#the rest of the linked list
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    #  this is the Function to initialize head
    def __init__(self):
        self.head = None

    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # this is just a function   to print the LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next


#  this is the driver codeDriver code
llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)

print(" for the Given linked list")
llist.printList()
llist.reverse()
print("\nThe Reversed linked list")
llist.printList()

