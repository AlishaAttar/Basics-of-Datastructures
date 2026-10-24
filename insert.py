


class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class LinkedList:
    def __init__(self):        
        self.head=None
    def append(self,new_node):
        if (self.head==None):
            self.head=new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node #appending new node
    def insert(self,new_node,pos):
         if pos==1:#inserting at first position
            new_node.next=self.head
            self.head=new_node
         else:
             p=1
             while(p!=pos-1):
              temp=temp.next
              p+=1
             new_node.next=temp.next
             temp.next=new_node    
    def print(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
list=LinkedList()

list.append(Node(55))
list.append(Node(48))

list.insert(Node(100),1)
list.print()         

#reversing,concatanating,deleting a node

 
