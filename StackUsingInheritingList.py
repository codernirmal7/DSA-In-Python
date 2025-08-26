class Stack (list) :
    def is_empty (self) :
        return len(self) == 0
    
    def push (self , data) :
        super().append(data)
    
    def pop (self) :
        if not self.is_empty () :
            super().pop()
        else :
            raise IndexError("Stack is empty")
        
    def peek (self) :
        if not self.is_empty ():
            return self[-1]
        else :
            raise IndexError("Stack is empty")
        
    def size (self) :
        return len(self)
    
    def insert(self, index, object):
        raise AttributeError("'insert' is not present in Stack")
    
    
a = Stack()
a.push(1)
a.push(2)
a.push(3)
print(f"The size of the list is {a.size()}")
print(f"The peek element of the list is {a.peek()}")
a.pop()
print(f"After Poped size of the list is {a.size()}")