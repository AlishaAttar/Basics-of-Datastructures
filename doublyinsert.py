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
    def insert(self,new_node,pos):
        temp=self.head
        if pos==1:
            new_node.next=self.head
            self.head.prev=new_node
        else:
            p=1
            while p!=pos-1:
                temp=temp.next
                p+=1
            new_node.next=temp.next
            temp.next=new_node
            new_node.prev=temp
            
            if temp.next:  #for last position              
                temp.next.prev=new_node 
            temp.next=new_node
            new_node.prev=temp

 
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
ll.insert(Node(12),4)
 
ll.print() 