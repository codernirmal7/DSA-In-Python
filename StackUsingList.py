class Stack :
    def __init__(self):
        self.list = []

    def is_empty (self) :
        return len(self.list) == 0
    
    def push (self , item) :
        self.list.append(item)

    def pop (self) :
        if not self.is_empty() :
            self.list.pop()
        else :
            raise IndexError("Stack is empty")
        
    def peek (self) :
        if not self.is_empty() :
            return self.list[-1]
        else :
            raise IndexError("Stack is empty")
        
    def size (self) :
        return len(self.list)
    


a = Stack()
a.push(1)
a.push(2)
a.push(3)
print(f"The size of the list is {a.size()}")
print(f"The peek element of the list is {a.peek()}")
a.pop()
print(f"After Poped size of the list is {a.size()}")