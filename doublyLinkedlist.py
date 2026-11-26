class Node: 
    def __init__(self, val): 
        self.data = val 
        self.next = None 
 
 
class LinkedList: 
    def __init__(self): 
        self.head = None 
 
    def append(self, new_node): 
        temp=self.head
        if temp:
            while temp.next:
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp       
        else: #first node
            self.head=new_node
 
    def print(self): 
        temp = self.head 
        while temp: 
            print(temp.data, end=" ") 
            temp = temp.next 
        print() 
 

ll = LinkedList() 
 
ll.append(Node(10)) 
ll.append(Node(20)) 
ll.append(Node(30)) 
ll.append(Node(40)) 
 
ll.print()