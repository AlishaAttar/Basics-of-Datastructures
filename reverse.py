


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
    def del_node(self,val):
        temp=self.head
        prev=None
        if temp.data==val:
            self.head=self.head.next
            return
        while(temp):
            if temp.data==val:#searching value
                break
            else:   #traverse
                prev=temp
                temp=temp.next
        if temp==None:
            print("Value is not present in the list")
        prev.next=temp.next    
    def reverse(self):
        curr=self.head
        prev=None
        while(curr):
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode
        self.head=prev    
                    

    def print(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
list=LinkedList()
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)

list.append(n1)
list.append(n2)
list.append(n3)
list.append(n4)
list.append(Node(55))
list.append(Node(48))

list.reverse()


list.print()         

#reversing,concatanating,deleting a node

 
