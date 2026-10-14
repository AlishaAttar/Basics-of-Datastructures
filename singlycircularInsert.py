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
    def insert(self,new_node,pos):
        if pos==1:
            temp=self.head
            while(temp.next!=self.head):
                temp=temp.next
            new_node.next=self.head
            self.head=new_node
            temp.next=self.head    
        else:#insert node from 2nd to last position
            p=1
            temp=self.head
            while(p!=pos-1):
                temp=temp.next
                p+=1
                new_node.next=temp .next
                temp.next=new_node   

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
ll.insert(Node(50),3)

 
ll.print()