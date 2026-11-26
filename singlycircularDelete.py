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
    def delete(self,val):
        temp=self.head
        prev=None
        if temp.data==val:
            while(temp.next!=self.head):
                temp=temp.next
            self.head=self.head.next
            temp.next=self.head
        else:
            while(temp.data!=val and temp):
                prev=temp
                temp=temp.next
                if temp==None:
                    print("Value is not present in the list")
                    return
            prev.next=temp.next
            temp=None    

                          
    

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
ll.delete(10)


 
ll.print()