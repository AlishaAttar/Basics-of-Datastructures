class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def append(self,new_node):
        if self.head== None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node
    def prepend(self,new_node) :
        
        new_node.next=self.head
        self.head=new_node  
    def delete(self,key):
        temp=self.head
        #delete head node
        if temp and temp.data==key :
            temp.next=self.head
            temp=None
            return


    def print(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
            
        print()
ll=linkedlist()
ll.append(Node(10)) 
ll.append(Node(20))
ll.append(Node(22))
ll.prepend(Node(11))
ll.delete(Node(11))
ll.print()           



            