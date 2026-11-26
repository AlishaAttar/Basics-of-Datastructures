class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def delete(self, val):
        temp = self.head

        if temp and temp.data == val:
            self.head = temp.next
            return

        while temp and temp.next:
            if temp.next.data == val:
                temp.next = temp.next.next
                return
            temp = temp.next


ll = LinkedList()
ll.append(Node(10))
ll.append(Node(20))
ll.append(Node(30))
ll.append(Node(40))

ll.delete(30)
ll.print()
