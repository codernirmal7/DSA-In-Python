from SinglyLinkedList import *

class Stack :
    def __init__(self):
        self.mylist = SLL()
        self.___list_length = 0

    def is_empty (self) :
        return self.___list_length == 0
    
    def push (self , data) :
        self.mylist.insert_at_start(data)
        self.___list_length +=1

    def pop (self) :
        self.mylist.delete_last()
        self.___list_length -=1

    def peek (self) :
        return self.mylist.start.item
    
    def size (self) :
        return self.___list_length
    

def main () :
    a = Stack()
    a.push(1)
    a.push(2)
    a.push(3)
    print(f"The size of the list is {a.size()}")
    print(f"The peek element of the list is {a.peek()}")
    a.pop()
    print(f"After Poped size of the list is {a.size()}")


if __name__ == "__main__" :
    main()