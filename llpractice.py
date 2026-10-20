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
ll.print()           



            