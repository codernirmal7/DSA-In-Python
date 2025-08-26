class DEQUEUE :
    def __init__(self):
        self.my_list = []

    def is_empty (self) :
        return len(self.my_list) == 0
    
    def size (self) :
        return len(self.my_list)
    
    def insert_rear (self , data) :
        self.my_list.append(data)

    def insert_front (self , data) :
        self.my_list.insert(0 , data)

    def delete_front (self) :
        if not self.is_empty() :
            self.my_list.pop(0)
        else :
            raise IndexError("Dequeue is empty")
        
    def delete_rear (self) :
        if not self.is_empty() :
            self.my_list.pop()
        else :
            raise IndexError("Dequeue is empty")
        
    
    def get_rear (self) :
        if not self.is_empty() :
            return self.my_list[-1]
        else :
            raise IndexError("Dequeue is empty")
        

    def get_front (self) :
        if not self.is_empty() :
            return self.my_list[0]
        else :
            raise IndexError("Dequeue is empty")
        

dequeue = DEQUEUE()
dequeue.insert_front(2)
dequeue.insert_front(3)
dequeue.insert_front(4)
dequeue.insert_rear(1)
print(dequeue.my_list)
dequeue.delete_front()
print("After deleting front")
print(dequeue.my_list)
dequeue.delete_rear()
print("After deleting rear")
print(dequeue.my_list)

print(f"Size of Dequeue : {dequeue.size()}")