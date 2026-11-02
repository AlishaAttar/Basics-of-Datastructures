#Create a Stack with following operations 
#1. Push 
#2. Pop 
#3. Display 
#4. Reverse String using Stack 
#5. Reverse Stack using another Stack



class Stack:
    def __init__(self):
        self.stack = []

    
    def push(self, val):
        self.stack.append(val)

    
    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Popped element:", self.stack.pop())

    
    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Stack elements:")
            for i in range(len(self.stack)-1, -1, -1):
                print(self.stack[i])

    
    def reverse_string(self, s):
        temp = []

        for i in s:
            temp.append(i)

        rev = ""

        while len(temp) > 0:
            rev = rev + temp.pop()

        print("Reversed string:", rev)

    
    def reverse_stack(self):
        temp = []

        while len(self.stack) > 0:
            temp.append(self.stack.pop())

        while len(temp) > 0:
            self.stack.append(temp.pop())

        print("Stack reversed")



s = Stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

print("Original stack:")
s.display()

s.pop()

print("After pop:")
s.display()

s.reverse_string("hello world")

s.reverse_stack()

print("After reversing stack:")
s.display()
