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
            new_node.next=self.head
        else: #for traversing the list
            temp = self.head 
            while (temp.next!=self.head): 
                temp = temp.next 
            temp.next = new_node 
            new_node.next=self.head

    def print(self): 
        temp = self.head 
        while (True): 
            print(temp.data, end=" ") 
            temp = temp.next 
            if temp==self.head:
                break
        print() 
 

ll = LinkedList() 
 
ll.append(Node(10)) 
ll.append(Node(20)) 
ll.append(Node(30)) 
ll.append(Node(40)) 
 
ll.print()