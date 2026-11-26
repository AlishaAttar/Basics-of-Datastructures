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

    def middle_del(self):
        temp=temp1=self.head
        prev=None
        while temp1 and temp1.next:
            prev=temp
            temp=temp.next
            temp1=temp1.next.next
        print("Middle node:",temp.data)
        prev.next=temp.next
        temp=None
    def delFirst_Last(self):
        temp1=self.head 
        temp1=None
        prev=None
        temp=self.head=self.head.next
        while(temp.next):
            prev=temp 
            temp=temp.next
        prev.next=None
        temp=None
    def print(self):
        print("List elements:")
              
    
        

ll = LinkedList()
ll.append(Node(10))
ll.append(Node(20))
ll.append(Node(30))
ll.append(Node(40))
ll.append(Node(50))


ll.delFirst_Last()
