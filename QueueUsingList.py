class Queue :
    def __init__(self):
         self.___my_list = []

    def is_empty (self) :
         return len(self.___my_list) == 0

    def size (self) :
         return len(self.___my_list)

    def insertion (self , data) :
        self.___my_list.append(data)

    def deletion (self) :
        if not self.is_empty() :
              self.___my_list.pop(0)
        else :
             raise IndexError("Queue Underflow")

    def getFIFO (self) :
         return self.___my_list[0]
    
    def print_items (self) :
         for i in self.___my_list :
              print(i , end=" ")


if __name__ == "__main__" :
     my_list = Queue()
     print("Inserting 1,2,3,4,5")
     my_list.insertion(1)
     my_list.insertion(2)
     my_list.insertion(3)
     my_list.insertion(4)
     my_list.insertion(5)
     my_list.print_items()
     print(f"FIFO : {my_list.getFIFO()}")
     my_list.deletion()
     print("After deletion")
     my_list.print_items()