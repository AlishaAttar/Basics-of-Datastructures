#Linea queue using linked list
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class Lqueue:
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node
    def dequeue(self):
        temp=self.front
        print("Deleted Node:",temp.data)
        self.front=self.front.next
        temp=None        
        if self.front==None:
            print("Queue is empty")
            self.rear=None
    def print(self):
        temp=self.front
        while temp:
            print(temp.data,end="->")
            temp=temp.next 
        print()           
que=Lqueue()
que.enqueue(Node(22))
que.enqueue(Node(32))
que.enqueue(Node(12))
que.enqueue(Node(25))
que.print()
que.dequeue()

