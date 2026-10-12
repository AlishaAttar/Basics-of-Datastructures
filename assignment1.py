class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create linked list / append node
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # 2. Print linked list
    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    # 3. Insert node at a specific position
    def insert(self, val, pos):
        new_node = Node(val)

        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for i in range(pos - 1):
            if temp is None:
                return
            temp = temp.next

        if temp is None:
            return

        new_node.next = temp.next
        temp.next = new_node

    # 4. Find middle node
    def middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow:
            print(slow.data)

    # 5. Delete a node by value
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

    # 6. Reverse linked list
    def reverse(self):
        prev = None
        temp = self.head

        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node

        self.head = prev

    # 7. Sum of every two consecutive nodes
    def pair_sum(self):
        temp = self.head

        while temp and temp.next:
            print(temp.data + temp.next.data, end=" ")
            temp = temp.next
        print()


# Main program
ll = LinkedList()

ll.append(Node(10))
ll.append(Node(20))
ll.append(Node(30))
ll.append(Node(40))

print("Linked list:")
ll.print()

print("Insert 25 at position 2:")
ll.insert(25, 2)
ll.print()

print("Middle node:")
ll.middle()

print("Delete 25:")
ll.delete(25)
ll.print()

print("Reverse list:")
ll.reverse()
ll.print()

print("Sum of consecutive nodes:")
ll.pair_sum()